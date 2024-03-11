#!/usr/bin/env python
# encoding=utf-8

# author        : Juno Park
# created date  : 2024.02.24
# modified date : 2024.02.24
# description   :

from PySide2 import QtWidgets, QtGui, QtCore
import uuid
import functools
import time


class Signals(QtCore.QObject):
    progress = QtCore.Signal(str, int)
    started = QtCore.Signal(bool)
    finished = QtCore.Signal(bool)


class WorkerThread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        self.thread_data = dict()
        self.t_id = uuid.uuid4().hex

    def run(self):
        self.signals.started.emit(True)
        num = 0

        while num <= 100:
            self.signals.progress.emit(self.t_id, num)
            num += 1
            time.sleep(0.2)
        self.signals.finished.emit(True)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        w = QtWidgets.QWidget()

        # variables
        self.__threads = list()
        self.thread_data = dict()
        self.th_cnt = 0

        self.progress = QtWidgets.QProgressBar()
        btn_start = QtWidgets.QPushButton('Start')
        btn_stop = QtWidgets.QPushButton('Stop')

        hbox_btns = QtWidgets.QHBoxLayout()
        hbox_btns.addWidget(btn_start)
        hbox_btns.addWidget(btn_stop)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.progress)
        vbox.addLayout(hbox_btns)

        w.setLayout(vbox)
        self.setCentralWidget(w)

        self.threadpool = QtCore.QThreadPool()
        print(f'maximum threads: ', self.threadpool.maxThreadCount())

        btn_start.pressed.connect(self.start_thread)


    def start_thread(self):
        thread = WorkerThread()
        if self.th_cnt < self.threadpool.maxThreadCount():
            self.th_cnt += 1
        else:
            self.th_cnt = self.threadpool.maxThreadCount()
            print('스레드를 더 이상 실행할 수 없습니다.')
        thread.signals.started.connect(self.slot_started)
        thread.signals.finished.connect(self.slot_finished)
        thread.signals.progress.connect(functools.partial(self.update_progress))

        self.__threads.append(thread)
        self.threadpool.start(thread)

    def update_progress(self, t_id, val):
        self.thread_data[t_id] = val
        val_lst = list(self.thread_data.values())
        total_num = sum(val_lst)
        ratio = int(total_num / len(self.thread_data))
        print(f'진행률: {ratio}% / 현재 실행된 스레드: {self.th_cnt}개')
        self.progress.setValue(ratio)

    def slot_started(self):
        print('start thread')

    def slot_finished(self):
        print('finished thread')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    rn = MainWindow()
    rn.show()
    app.exec_()