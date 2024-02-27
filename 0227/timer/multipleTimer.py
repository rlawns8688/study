#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.24
# modified date : 2024.02.24
# description   :

# bitfield 적용
# 시작-재시작
# combobox 적용
import sys
import uuid
import typing
import pathlib
import functools
from PySide2 import QtWidgets, QtGui, QtCore
from pydantic import BaseModel
from resources.ui import timer_template_ui
from libs.system import library as sys_lib



class Constant:
    # read-only로 만들기 위함.
    __slots__ = ()
    # bit index
    # 0000 0001
    START: typing.Final[int] = 1
    # 0000 0010
    PAUSE: typing.Final[int] = 2
    # 0000 0100
    STOP: typing.Final[int] = 4

    # 0000 0100 -> stop status
    # 0000 0001 -> start status
    # 0000 0010 -> pause status

Constant = Constant()


# data class
# class Data(BaseModel):
#     secs: int
#     accum_num: int
#     ratio: float
#
#
# class Signals(QtCore.QObject):
#     sig_data = QtCore.Signal(Data)




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
        self.__signals: Signals = Signals()
        self.__bitfield: BitMask = BitMask()
        self.__total_num: int = 0
        self.__condition = QtCore.QWaitCondition()
        self.__mutex = QtCore.QMutex()

        # init
        # 0000 0100
        self.__bitfield.activate(Constant.STOP)
        # 0000 0111
        self.__bitfield.deactivate(Constant.START | Constant.PAUSE)
        # 0000 0001 | 0000 0010  => 0000 0011
        # 0000 0100

    @property
    def signals(self):
        return self.__signals

    @property
    def bitfield(self):
        return self.__bitfield

    def resume(self):
        self.__condition.wakeAll()

    def run(self):
        num = 0
        while num <= self.__total_num:
            if self.bitfield.confirm(Constant.STOP):
                break
            try:
                ratio = int((num / self.__total_num) * 100)
            except ZeroDivisionError as err:
                ratio = 0
            self.signals.emit(self.w_id,ratio)
            self.__mutex.lock()
            num += 1
            if self.bitfield.confirm(Constant.PAUSE):
                self.__condition.wait(self.__mutex)
            self.__mutex.unlock()
            self.sleep(1)

    def stop(self):
        self.bitfield.activate(Constant.STOP)
        if self.bitfield.confirm(Constant.PAUSE):
            self.resume()
        self.bitfield.deactivate(Constant.START | Constant.PAUSE)
        self.quit()
        self.wait(5000)
        # self.deleteLater()

    def run_start(self, total_num: int):
        if self.bitfield.confirm(Constant.START | Constant.PAUSE):
            self.bitfield.toggle(Constant.START | Constant.PAUSE)
        else:
            if not self.bitfield.confirm(Constant.START | Constant.PAUSE):
                self.bitfield.activate(Constant.START)
        self.bitfield.deactivate(Constant.STOP)
        self.__total_num = total_num
        self.start()




class MultipleTimer(QtWidgets.QMainWindow,timer_template_ui.Ui_Form):
    CMDS_SET = {
        'Run Houdini': '/opt/hfs19.5/bin/houdini',
        'Run Firefox': '/usr/bin/firefox',
        'Run Terminal': '/usr/bin/gnome-terminal'
    }
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        w = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.__work_thread = WorkerThread(w_id=None)
        # var
        self.__cnt_widgets = 3
        self.__widget_data = dict()
        self.__thread_data = dict()

        self.set_widgets()
        self.set_threads()

        w.setLayout(self.vbox)
        self.setCentralWidget(w)

        self.pushButton__start.clicked.connect(self.slot_start_timer)
        self.pushButton__stop.clicked.connect(self.slot_stop_timer)
        self.comboBox__cmd.addItems(list(MultipleTimer.CMDS_SET.keys()))
        # w.pushButton__start.pressed.connect(functools.partial(self.slot_btn_start, w_id))
        #
    @staticmethod
    def open_file_using_thread(
            cmdpath: pathlib.Path, filepath: typing.Union[pathlib.Path, None], with_term: bool = False) -> bool:
        assert isinstance(cmdpath, pathlib.Path)
        if (filepath is not None) and (not filepath.exists()):
            sys.stderr.write('"{0}" 오픈하려는 파일을 찾을 수 없습니다.'.format(filepath.as_posix()))
            return False
        if not cmdpath.exists():
            sys.stderr.write(f'{cmdpath.as_posix()} 실행 파일을 찾을 수 없습니다.')
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

    @QtCore.Slot(str, int)
    def update_progress(self, w_id, ratio):
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        w.progressBar.setValue(ratio)

        if ratio == 100:
            self.run_commands()
    def run_commands(cmd):
        # sys_lib.System.open_file_using_thread(pathlib.Path(cmd), None, False)
        cmds = self.get_commands()
        if not len(cmds):
            return
        for cmd in cmds:
            sys_lib.System.open_file_using_thread(pathlib.Path(MultipleTimer.CMDS_SET.get(cmd)), None, False)

    def get_commands(self):
        cnt_items = self.listWidget__command.count()
        # Drag & Drop 사용할 때...
        # return [str(self.listWidget__command.item(i).text()) for i in range(cnt_items)]
        return [self.listWidget__command.item(i).current_text for i in range(cnt_items)]
    def finished_thread(self, w_id):
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        th: WorkerThread = self.__thread_data[w_id]
        cmd = w.lineEdit__cmd.text()
        if not len(cmd.strip()):
            QtWidgets.QMessageBox.warning(self, 'Warning', '{0} 명령어 입력하세요.'.format(w_id))
            return
        if not th.stop():
            MultipleTimer.run_commands(cmd)
    # @QtCore.Slot(Data)
    # def slot_update_ui(self, data: Data):
    #     self.progressBar__remaining.setValue(data.ratio)
    #     self.lcdNumber__remaining.display(SingleTimer.secs2qtime(data.secs).toString())
    #
    #     if data.secs <= 0:
    #         self.run_commands()


    def slot_btn_start(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        # start thread
        th.run_start(MultipleTimer.qtime2secs(w.timeEdit__timer.time()))

    def slot_btn_stop(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        th.stop()






    def slot_start_timer(self):
        if MultipleTimer.qtime2secs(self.timeEdit__timer.time()) <= 0:
            QtWidgets.QMessageBox.warning(self, 'Warning', '타이머 설정을 해야 합니다.')
            return
        if not self.__work_thread.isRunning():
            # start
            self.__work_thread.run_start(self.qtime2secs(self.timeEdit__timer.time()))
            self.timeEdit__timer.setEnabled(False)
            if self.__work_thread.bitfield.confirm(Constant.START | Constant.PAUSE):
                self.pushButton__start.setText('일시 정지')
                if self.__work_thread.bitfield.confirm(Constant.PAUSE):
                    self.pushButton__start.setText('  시작  ')
        else:
            self.__work_thread.bitfield.toggle(Constant.START | Constant.PAUSE)
            if not self.__work_thread.bitfield.confirm(Constant.PAUSE):
                self.__work_thread.resume()
                self.pushButton__start.setText('일시 정지')
            else:
                self.pushButton__start.setText('  재시작  ')

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


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mt = MultipleTimer()
    mt.show()
    app.exec_()
