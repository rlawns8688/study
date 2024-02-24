import time
import uuid
import functools
from PySide2 import QtCore, QtGui, QtWidgets

class Signals(QtCore.QObject):
    progress = QtCore.Signal(int)
    started = QtCore.Signal(bool)
    finished = QtCore.Signal(bool)



class WorkerThread(QtCore.QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        self.count_id = int
        self.w_list = list()


    def run(self):
        self.signals.started.emit(True)
        num = 0
        while num <= 100:
            self.signals.progress.emit(num)
            num += 1
            time.sleep(0.2)
            # time sleep과 thread sleep의 차이는 ?? 똑같음.
        self.signals.finished.emit(True)

class MainWindow(QtWidgets.QMainWindow):
      def __init__(self):
        super().__init__()
        w = QtWidgets.QWidget()

        self.id_counter = 0
        self.progress_counter = 0

        # variable
        self.__thread = list()

        self.progress = QtWidgets.QProgressBar()
        btn_start = QtWidgets.QPushButton('start')
        btn_stop = QtWidgets.QPushButton('stop')

        hbox_btns = QtWidgets.QHBoxLayout()
        hbox_btns.addWidget(btn_start)
        hbox_btns.addWidget(btn_stop)

        vbox_prog= QtWidgets.QVBoxLayout()
        vbox_prog.addWidget(self.progress)
        vbox_prog.addLayout(hbox_btns)

        w.setLayout(vbox_prog)
        self.setCentralWidget(w)

        self.threadpool = QtCore.QThreadPool()

        print('Maximum thread : ',self.threadpool.maxThreadCount())
        btn_start.pressed.connect(self.start_thread)

      def start_thread(self):

            thread = WorkerThread()
            thread.signals.started.connect(self.slot_started)
            thread.signals.finished.connect(self.slot_finished)
            thread.signals.progress.connect(self.slot_progress)
            self.__thread.append(thread)
            self.threadpool.start(thread)

            print(self.__thread)

      def slot_progress(self, val):
            self.progress_counter += val  # 진행 상태를 카운팅합니다.
            average_progress = self.progress_counter / self.id_counter
            self.progress.setValue(average_progress if average_progress <= 100 else 100)

      def slot_started(self):
            self.id_counter += 1
            print(f'thread count:  {self.id_counter}')

      def slot_finished(self):
            self.id_counter -= 1  # 완료된 쓰레드의 수를 감소시킵니다.
            if self.id_counter == 0:
                self.progress.setValue(100)
            print('finished thread')

            # thread 연결하기
            # pressed와 click의 차이 = pressed는 버튼을 누르고 있는 상태로 만드는 것
            # click은

            # btn_start.pressed.
            # btn_stop




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    mw = MainWindow()
    mw.show()
    app.exec_()