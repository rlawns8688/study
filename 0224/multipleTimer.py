#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.24
# modified date : 2024.02.24
# description   :

import uuid
import pathlib
import functools
import pathlib


from PySide2 import QtWidgets, QtGui, QtCore

from resources.ui import timer_template_ui
from libs.system import library as sys_lib


class Signals(QtCore.QObject):
    progress = QtCore.Signal(str, int)



class WorkerThread(QtCore.QThread):
    def __init__(self, w_id):
        super().__init__()
        self.w_id = w_id #set_widgets 에서 받은 위젯 id
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
        self.resize(600,700)



    def set_widgets(self):
        for i in range(self.__cnt_widgets):
            w_id = uuid.uuid4().hex
            widget = QtWidgets.QWidget()
            w = timer_template_ui.Ui_Form()

            w.setupUi(widget)
            self.vbox.addWidget(widget)

            w.pushButton__start.pressed.connect(functools.partial(self.slot_btn_start, w_id))
            w.pushButton__stop.pressed.connect(functools.partial(self.slot_btn_stop, w_id))
            #
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
        th: WorkerThread = self.__thread_data[w_id]
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        cmd = w.lineEdit__cmd.text()
        if not len(cmd.strip()):
            QtWidgets.QMessageBox.warning(self,'Warning {0}'.format(w_id))
            return
        if not th.is_stop:
            MultipleTimer.run_commands(cmd)
    @QtCore.Slot(str, int)
    def update_progress(self, w_id, val):
        #위젯 자체를 id 하나씩 부여했기 때문에 해당 id의 위젯의 progress로 들어가야됌
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        print(val)
        w.progressBar.setValue(val)


    def slot_btn_start(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        w: timer_template_ui.Ui_Form = self.__widget_data[w_id]
        # start thread
        th.run_start(MultipleTimer.qtime2secs(w.timeEdit__timer.time()))

    def slot_btn_stop(self, w_id):
        th: WorkerThread = self.__thread_data[w_id]
        th.stop()


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