#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.21
# modified date : 2024.02.21
# description   :

import time
import uuid
import random

from PySide2 import QtWidgets, QtGui, QtCore


class Status:
    waiting = 'waiting'
    running = 'running'
    error = 'error'
    complete = 'complete'
    stopped = 'stopped'

    class Keys:
        status = 'status'
        progress = 'progress'


class Default:
    data = {Status.Keys.status: Status.waiting, Status.Keys.progress: 0}


class Colors:
    status = {
        Status.running: '#329DA8',
        Status.error: '#A83632',
        Status.stopped: '#DDDDDD',
        Status.complete: '#32A848'
    }


class WorkerKilledException(Exception): ...


class WorkerSignals(QtCore.QObject):
    '''
    워커 스레드에 사용할 시그널 정의
    '''

    error = QtCore.Signal(str, str)
    result = QtCore.Signal(str, object)

    finished = QtCore.Signal(str)
    progress = QtCore.Signal(str, int)
    status = QtCore.Signal(str, str)


class Worker(QtCore.QRunnable):
    '''
    워커 스레드
    '''

    def __init__(self, *args, **kwargs):
        super().__init__()

        # 워커 스레드가 사용할 시그널
        self.signals = WorkerSignals()

        # 각 작업의 대한 유니크한 ID 설정
        self.jobid = uuid.uuid4().hex

        self.args = args
        self.kwargs = kwargs

        self.signals.status.emit(self.jobid, Status.waiting)

        self.is_killed = False

    def run(self):
        self.signals.status.emit(self.jobid, Status.running)

        x, y = self.args

        try:
            value = random.randint(0, 100) * x
            delay = random.random() / 10
            result = list()

            for i in range(100):
                # 명시적으로 divide by zero 에러 발생 시킴
                value = value / y
                y -= 1

                result.append(value)

                self.signals.progress.emit(self.jobid, i + 1)
                time.sleep(delay)

                if self.is_killed:
                    raise WorkerKilledException
        except WorkerKilledException:
            self.signals.status.emit(self.jobid, Status.stopped)

        except Exception as err:
            print(err)
            self.signals.error.emit(self.jobid, str(err))
            self.signals.status.emit(self.jobid, Status.error)

        # 예외가 발생하지 않았다면
        else:
            self.signals.result.emit(self.jobid, result)
            self.signals.status.emit(self.jobid, Status.complete)

        self.signals.finished.emit(self.jobid)

    def kill(self):
        self.is_killed = True


class WorkerManager(QtCore.QAbstractListModel):
    '''
    워커 대기열 및 상태를 처리하는 관리자
    각 워커의 진행 상황을 표시
    '''

    _workers = dict()
    _state = dict()

    status = QtCore.Signal(str)

    def __init__(self):
        super().__init__()

        self.threadpool = QtCore.QThreadPool()
        self.max_threads = self.threadpool.maxThreadCount()
        print('maximum thread: {0}'.format(self.max_threads))

        self.status_timer = QtCore.QTimer()
        self.status_timer.setInterval(100)
        self.status_timer.timeout.connect(self.notify_status)

    def notify_status(self):
        n_workers = len(WorkerManager._workers)
        running = min(n_workers, self.max_threads)
        waiting = max(0, n_workers - self.max_threads)
        self.status.emit(f'running: {running}, waiting: {waiting}, maximum thread: {self.max_threads}')

    @QtCore.Slot(str, str)
    def slot_receive_status(self, jobid, status):
        WorkerManager._state[jobid][Status.Keys.status] = status
        self.layoutChanged.emit()

    @QtCore.Slot(str, int)
    def slot_receive_progress(self, jobid, progress):
        WorkerManager._state[jobid][Status.Keys.progress] = progress
        self.layoutChanged.emit()

    @QtCore.Slot(str, str)
    def slot_receive_error(self, jobid, msg):
        print(jobid, msg)

    @QtCore.Slot(str)
    def slot_done(self, jobid):
        del WorkerManager._workers[jobid]
        self.layoutChanged.emit()

    def enqueue(self, worker: Worker):
        '''
        워커를 QThreadPool에 전달해 실행할 워커를 대기열에 넣는다.
        '''
        worker.signals.error.connect(self.slot_receive_error)
        worker.signals.status.connect(self.slot_receive_status)
        worker.signals.progress.connect(self.slot_receive_progress)
        worker.signals.finished.connect(self.slot_done)

        self.threadpool.start(worker)
        WorkerManager._workers[worker.jobid] = worker
        WorkerManager._state[worker.jobid] = Default.data.copy()

        self.layoutChanged.emit()

    def cleanup(self):
        '''
        worker_state에서 완료 또한 실패한 워커 제거
        '''

        for jobid, ste in list(WorkerManager._state.items()):
            if ste[Status.Keys.status] in (Status.complete, Status.error):
                del WorkerManager._state[jobid]
        self.layoutChanged.emit()

    @staticmethod
    def kill(jobid):
        if jobid in WorkerManager._workers:
            WorkerManager._workers[jobid].kill()

    # model interface
    def data(self, index, role=...):
        if role == QtCore.Qt.DisplayRole:
            jobids = list(WorkerManager._state.keys())
            jobid = jobids[index.row()]
            return jobid, WorkerManager._state[jobid]

    def rowCount(self, parent=...):
        return len(WorkerManager._state)


class ProgressbarDelegate(QtWidgets.QStyledItemDelegate):
    """
    QListView에 프로그레스바 표시를 위한 델리게이트
    리스트 뷰는 각 행을 텍스트 값으로 표시하는데, 이것을 텍스트가 아닌 프로그레스로 그리도록...
    """
    def paint(self, painter, option, index):
        jobid, data = index.model().data(index, QtCore.Qt.DisplayRole)
        if data[Status.Keys.progress] > 0:
            color = QtGui.QColor(Colors.status[data[Status.Keys.status]])
            brush = QtGui.QBrush()
            brush.setColor(color)
            brush.setStyle(QtCore.Qt.SolidPattern)

            width = option.rect.width() * data[Status.Keys.progress] / 100
            rect = QtCore.QRect(option.rect)
            rect.setWidth(width)
            painter.fillRect(rect, brush)

        pen = QtGui.QPen()
        pen.setColor(QtCore.Qt.black)
        painter.drawText(option.rect, QtCore.Qt.AlignLeft, jobid)

        if option.state & QtWidgets.QStyle.State_Selected:
            painter.drawRect(option.rect)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.workers = WorkerManager()
        self.workers.status.connect(self.statusBar().showMessage)

        layout = QtWidgets.QVBoxLayout()

        self.progress = QtWidgets.QListView()
        self.progress.setModel(self.workers)
        delegate = ProgressbarDelegate()
        self.progress.setItemDelegate(delegate)

        layout.addWidget(self.progress)

        self.text = QtWidgets.QPlainTextEdit()
        self.text.setReadOnly(True)

        start = QtWidgets.QPushButton('Start')
        start.pressed.connect(self.start_worker)

        stop = QtWidgets.QPushButton('Stop')
        stop.pressed.connect(self.stop_worker)

        clear = QtWidgets.QPushButton('Clear')
        clear.pressed.connect(self.workers.cleanup)

        layout.addWidget(self.text)
        layout.addWidget(start)
        layout.addWidget(stop)
        layout.addWidget(clear)

        w = QtWidgets.QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

    def start_worker(self):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)

        w = Worker(x, y)
        w.signals.result.connect(self.display_result)
        w.signals.error.connect(self.display_result)

        self.workers.enqueue(w)

    def stop_worker(self):
        selected = self.progress.selectedIndexes()
        for idx in selected:
            jobid, _ = self.workers.data(idx, QtCore.Qt.DisplayRole)
            self.workers.kill(jobid)

    def display_result(self, jobid, data):
        self.text.appendPlainText(f'worker: {jobid}, {data}')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec_()


































