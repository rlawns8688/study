#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.24
# modified date : 2024.02.24
# description   :

# bitfield 적용
# 시작-재시작
# combobox 적용

import uuid
import typing
import pathlib
import functools
from PySide2 import QtWidgets, QtCore

from resources.ui import timer_template_ui
from libs.system import library as sys_lib





class BitMask:
    FIELD = 0b0000
    __INSTANCE = None

    def __new__(cls, *args, **kwargs) -> typing.Any:
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(BitMask, cls).__new__(cls, *args, **kwargs)
        return cls.__INSTANCE

    def __str__(self) -> str:
        bits = list()
        digits = 8
        for i in range(digits):
            bits.append(str((self.__INSTANCE.FIELD >> (digits - 1 - i)) & 0x01))
            if ((i + 1) % 4) == 0:
                bits.append(' ')
        return ''.join(bits)

    @classmethod
    def __activate(cls, num: int) -> None:
        cls.__INSTANCE.FIELD |= (0x01 << num)

    @classmethod
    def __deactivate(cls, num: int) -> None:
        cls.__INSTANCE.FIELD &= (~(0x01 << num))

    @classmethod
    def __toggle(cls, num: int) -> None:
        cls.__INSTANCE.FIELD ^= (0x01 << num)

    @classmethod
    def __confirm(cls, num: int) -> bool:
        return cls.__INSTANCE.FIELD & (0x01 << num)

    @classmethod
    def activate(cls, bitfield: int) -> None:
        cls.__INSTANCE.FIELD |= bitfield

    @classmethod
    def deactivate(cls, bitfield: int) -> None:
        cls.__INSTANCE.FIELD &= (~bitfield)

    @classmethod
    def toggle(cls, bitfield: int) -> None:
        cls.__INSTANCE.FIELD ^= bitfield

    @classmethod
    def confirm(cls, bitfield: int) -> bool:
        return bool(cls.__INSTANCE.FIELD & bitfield)

    @classmethod
    def confirm_onebit(cls, num: int) -> bool:
        return cls.__INSTANCE.FIELD & (0x01 << num)

    @classmethod
    def empty(cls) -> None:
        cls.__INSTANCE.FIELD = 0

    @classmethod
    def all(cls) -> None:
        cls.__INSTANCE.FIELD = -1


class Signals(QtCore.QObject):
    progress = QtCore.Signal(str, int)


class WorkerThread(QtCore.QThread):
    def __init__(self, w_id):
        super().__init__()
        self.w_id = w_id
        self.is_stop = True
        self.__total_num = 0
        self.signals = Signals()

    def run(self):
        num = 0
        while num <= self.__total_num:
            if self.is_stop:
                break
            try:
                ratio = int((num / self.__total_num) * 100)
            except ZeroDivisionError as err:
                ratio = 0
            self.signals.progress.emit(self.w_id, ratio)
            num += 1
            self.sleep(1)

    def run_start(self, total_num):
        self.__total_num = total_num
        self.is_stop = False
        self.start()

    def stop(self):
        self.is_stop = True


class MultipleTimer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        w = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()

        # var
        self.__cnt_widgets = 3
        self.__widget_data = dict()
        self.__thread_data = dict()

        self.set_widgets()
        self.set_threads()

        w.setLayout(self.vbox)
        self.setCentralWidget(w)

    @staticmethod
    def open_file_using_thread(
            cmdpath: pathlib.Path, filepath: typing.Union[pathlib.Path, None], with_term: bool = False) -> bool:
        assert isinstance(cmdpath, pathlib.Path)
        if (filepath is not None) and (not filepath.exists()):
            sys_lib.stderr.write('"{0}" 오픈하려는 파일을 찾을 수 없습니다.'.format(filepath.as_posix()))
            return False
        if not cmdpath.exists():
            sys_lib.stderr.write(f'{cmdpath.as_posix()} 실행 파일을 찾을 수 없습니다.')
            return False
        t = threading.Thread(target=System.open_file_with_arguments, args=(cmdpath, filepath, with_term))
        t.daemon = True
        t.start()
        return True

    @staticmethod
    def open_file_with_arguments(
            cmdpath: pathlib.Path, filepath: typing.Union[pathlib.Path, None], with_term: bool = False) -> int:
        if filepath is not None:
            cmd = '{0} {1}'.format(cmdpath.as_posix(), filepath.as_posix())
        else:
            cmd = cmdpath.as_posix()
        if with_term:
            cmd = System.open_with_terminal(cmd)
        result = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = result.communicate()
        out = out.decode('utf8')
        exitcode = result.returncode
        if exitcode != 0:
            sys.stderr.write('{0}, {1}, {2}'.format(exitcode, out.decode('utf8'), err.decode('utf8')))
            return 127
        return exitcode

    def set_widgets(self):
        for i in range(self.__cnt_widgets):
            w_id = uuid.uuid4().hex
            widget = QtWidgets.QWidget()
            w = timer_template_ui.Ui_Form()
            w.setupUi(widget)
            self.vbox.addWidget(widget)

            w.pushButton__start.pressed.connect(functools.partial(self.slot_btn_start, w_id))
            w.pushButton__stop.pressed.connect(functools.partial(self.slot_btn_stop, w_id))

            self.__widget_data[w_id] = w

    def set_threads(self):
        for w_id, widget in self.__widget_data.items():
            th = WorkerThread(w_id)
            th.signals.progress.connect(functools.partial(self.update_progress))
            th.finished.connect(functools.partial(self.finished_thread, w_id))
            self.__thread_data[w_id] = th

    @staticmethod
    def run_commands(cmd):
        sys_lib.System.open_file_using_thread(pathlib.Path(cmd), None, False)

    def finished_thread(self, w_id):
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        th: WorkerThread = self.__thread_data[w_id]
        cmd = w.lineEdit__cmd.text()
        if not len(cmd.strip()):
            QtWidgets.QMessageBox.warning(self, 'Warning', '{0} 명령어 입력하세요.'.format(w_id))
            return
        if not th.is_stop:
            MultipleTimer.run_commands(cmd)

    @QtCore.Slot(str, int)
    def update_progress(self, w_id, val):
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        w.progressBar.setValue(val)

    def slot_btn_start(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        # start thread
        th.run_start(MultipleTimer.qtime2secs(w.timeEdit__timer.time()))

    def slot_btn_stop(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        th.stop()

    def time2sec(self):
        w: timer_template_ui.Ui_Form = self.__widget_data['0']
        return w.timeEdit__timer.time()

    @staticmethod
    def qtime2secs(qtime) -> int:
        h, m, s = qtime.hour(), qtime.minute(), qtime.second()
        total_sec = h * 3600 + m * 60 + s
        return total_sec

    @staticmethod
    def secs2qtime(secs: int) -> QtCore.QTime:
        h, m = divmod(secs, 3600)
        m = m // 60
        s = secs % 60
        return QtCore.QTime(h, m, s)

    @staticmethod
    def addition(a, b):
        return a + b


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mt = MultipleTimer()
    mt.show()
    app.exec_()