import time
from PySide2 import QtCore, QtGui, QtWidgets
import uuid

class Signals(QtCore.QObject):
    progress = QtCore.Signal(str, int)
    started = QtCore.Signal(bool)
    finished = QtCore.Signal(bool)


class WorkerThread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        self.id = uuid.uuid4().hex

    def run(self):
        self.signals.started.emit(True)
        num = 0
        while num <= 100:
            self.signals.progress.emit(self.id, num)
            num += 1
            time.sleep(0.2)
        self.signals.finished.emit(True)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = QtWidgets.QWidget()
        self.set_layout()
        # self.__threads = list()

        self.threadpool = QtCore.QThreadPool()
        print('maximum threads: ', self.threadpool.maxThreadCount())
        self.threads_progress = {}
        self.btn_start.pressed.connect(self.start_thread)

    def set_layout(self):
        self.progress = QtWidgets.QProgressBar()
        self.btn_start = QtWidgets.QPushButton('start')
        self.btn_stop = QtWidgets.QPushButton('stop')
        hbox_btns = QtWidgets.QHBoxLayout()
        hbox_btns.addWidget(self.btn_start)
        hbox_btns.addWidget(self.btn_stop)
        vbox_prog = QtWidgets.QVBoxLayout()
        vbox_prog.addWidget(self.progress)
        vbox_prog.addLayout(hbox_btns)
        self.w.setLayout(vbox_prog)
        self.setCentralWidget(self.w)

    def start_thread(self):
        thread = WorkerThread()
        thread.signals.started.connect(self.slot_started)
        thread.signals.finished.connect(self.slot_finished)
        thread.signals.progress.connect(self.slot_progress) # emit에서 보낸 값을 슬롯으로 받을 수 있게 해주는 연결
        # self.__threads.append(thread)
        self.threadpool.start(thread)

        # print(self.__threads)

    def slot_progress(self, id, val):
        self.threads_progress[id] = val # 딕셔너리에  id 와 val를 계속 최신화
        aver_progress = sum(self.threads_progress.values()) / len(self.threads_progress.keys())
        self.progress.setValue(int(aver_progress))
    def slot_started(self):
        print('start thread')

    def slot_finished(self):
        print('finished thread')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()