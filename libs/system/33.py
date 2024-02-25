import time

from PySide2 import QtCore, QtGui, QtWidgets
import functools
import uuid
class Signals(QtCore.QObject):
    progress = QtCore.Signal(str, int)
    started = QtCore.Signal(bool)
    finished = QtCore.Signal(bool)


class WorkerThread(QtCore.QRunnable):
    def __init__(self, w_id):
        super().__init__()
        self.w_id = w_id
        self.signals = Signals()

    def run(self):
        self.signals.started.emit(True)
        num = 0
        while num <= 100:
            num += 1
            time.sleep(0.2)
            self.signals.progress.emit(self.w_id, num)
            # if num >= num:
            #     print('hi')

            # time sleep과 thread sleep의 차이는 ?? 똑같음.
        self.signals.finished.emit(True)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        w = QtWidgets.QWidget()
        # self.__count_widget = 0
        # variable
        self.__thread = list()
        self.th_count = dict()
        self.__ratio = list()
        self.set_widgets()

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

    def set_widgets(self):
        for i in range(len(self.__thread)):
            w_id = uuid.uuid4().hex
            th = WorkerThread(w_id)
            th.signals.progress.connect(functools.partial(self.update_progress))
            self.__widget_data[w_id] = th


    @QtCore.Slot(str, int)
    def update_progress(self, w_id, val):
            w: MainWindow.Ui_Form = self.__widget_data[w_id]
            w.progressBar.setValue(val)

    def start_thread(self):
            thread = WorkerThread(self.w_id)
            thread.signals.started.connect(self.slot_started)
            thread.signals.finished.connect(self.slot_finished)
            thread.signals.progress.connect(functools.partial(self.update_progress))
            self.__thread.append(thread)
            self.threadpool.start(thread)

            print(len(self.__thread))



    def slot_progress(self, val):
        self.progress.setValue(val)

    def slot_started(self):
        # self.__count_widget += 1
        print('start thread')


    def slot_finished(self):
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