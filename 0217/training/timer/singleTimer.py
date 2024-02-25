#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
# author        : Seongcheol Jeon
# created date  : 2024.02.15
# modified date : 2024.02.15
# description   :

import sys
import typing
import importlib


import qdarktheme
from pydantic import BaseModel
from PySide2 import QtWidgets, QtGui, QtCore

from resources.ui import timer_ui
from libs.system import library as sys_lib
from libs.qt import library as qt_lib
from libs.qt import stylesheet
from libs.algorithm.library import BitMask

importlib.reload(timer_ui)
importlib.reload(sys_lib)
importlib.reload(qt_lib)
importlib.reload(stylesheet)
#

class BGImageStylesheet:
    bg_stylesheet = '''
    QWidget {
        background-image: url(':/images/images/borabora.jpg');
        background-repeat: no-repeat;
        background-position: center;
    } 
    '''


class Constant:
    # read-only로 만들기 위함.
    __slots__ = ()
    # bit index
    START: typing.Final[int] = 1
    PAUSE: typing.Final[int] = 2
    STOP: typing.Final[int] = 4


Constant = Constant()


# data class
class Data(BaseModel):
    secs: int
    accum_num: int
    ratio: float


class Signals(QtCore.QObject):
    sig_data = QtCore.Signal(Data)


class WorkThread(QtCore.QThread):
    def __init__(self):
        super().__init__()
        self.__signals: Signals = Signals()
        self.__bitfield: BitMask = BitMask()
        self.__total_num: int = 0
        self.__condition = QtCore.QWaitCondition()
        self.__mutex = QtCore.QMutex()

        # init
        self.__bitfield.activate(Constant.STOP)
        self.__bitfield.deactivate(Constant.START | Constant.PAUSE)

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
            self.signals.sig_data.emit(Data(secs=self.__total_num - num, accum_num=num, ratio=ratio))
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


class ComboBoxItem(QtWidgets.QListWidgetItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.combobox = QtWidgets.QComboBox()
        self.setSizeHint(self.combobox.sizeHint())
        self.__curt_text = ''
        self.__curt_index = -1
        self.combobox.currentIndexChanged.connect(self.slot_combobox_changed)

    def __hash__(self):
        return id(self)

    @QtCore.Slot(int)
    def slot_combobox_changed(self, index):
        self.__curt_text = self.combobox.currentText()
        self.__curt_index = index

    @property
    def current_text(self):
        return self.__curt_text

    @property
    def current_index(self):
        return self.__curt_index


class SingleTimer(QtWidgets.QWidget, timer_ui.Ui_Form__timer):
    CMDS_SET = {
        'Run Houdini': '/opt/hfs19.5/bin/houdini',
        'Run Firefox': '/usr/bin/firefox',
        'Run Terminal': '/usr/bin/gnome-terminal'
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        qdarktheme.setup_theme()
        self.setAutoFillBackground(True)
        # self.setStyleSheet(BGImageStylesheet.bg_stylesheet)
        # init
        self.__init_set_ui()
        self.__init_set()
        self.__work_thread = WorkThread()

        # connections
        self.pushButton__start.clicked.connect(self.slot_start_timer)
        self.pushButton__stop.clicked.connect(self.slot_stop_timer)
        self.__work_thread.signals.sig_data.connect(self.slot_update_ui)
        self.__work_thread.started.connect(self.slot_started_timer)
        self.__work_thread.finished.connect(self.slot_finished_timer)
        self.pushButton__add_item.clicked.connect(self.slot_add_item)
        self.pushButton__del_item.clicked.connect(self.slot_del_item)
        self.listWidget__command.doubleClicked.connect(self.slot_double_clk_item)

        # QTimer를 이용한...
        # self.timer = QtCore.QTimer(self)
        # self.timer.singleShot(10000, self.slot_single_shot)
        # self.timer2 = QtCore.QTimer(self)
        # self.timer2.start(1000)
        # self.timer2.timeout.connect(self.slot_timeout)

    # def slot_single_shot(self):
    #     print('run command')
    #     self.timer2.stop()

    # def slot_timeout(self):
    #     curt_time = QtCore.QDateTime.currentDateTime().toString('hh:mm:ss')
    #     self.lcdNumber__remaining.display(curt_time)

    def __init_set_ui(self):
        self.listWidget__command.setAlternatingRowColors(True)
        self.lcdNumber__remaining.setDigitCount(8)
        self.progressBar__remaining.setStyleSheet(stylesheet.ProgressBar.ORANGE_PROGRESS_STYLE)
        # Drag & Drop
        # self.listWidget__command.setDragEnabled(True)
        # self.listWidget__command.setAcceptDrops(True)
        # self.listWidget__command.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

    def __init_set(self):
        self.pushButton__start.setText('  시작  ')
        self.progressBar__remaining.setValue(0)
        self.timeEdit__timer.setEnabled(True)
        self.lcdNumber__remaining.display('00:00:00')

    @QtCore.Slot(QtCore.QModelIndex)
    def slot_double_clk_item(self, item: QtCore.QModelIndex):
        if not item.isValid():
            return
        print(item.data())

    @QtCore.Slot()
    def slot_add_item(self):
        # Drag & Drop 셋팅이면...
        # ok, text = qt_lib.QtLibs.input_dialog('실행 명령 추가', '명령문 입력', self)
        # if not (ok and text):
        #     return
        # item = QtWidgets.QListWidgetItem(text)

        item = ComboBoxItem()
        item.combobox.addItems(list(SingleTimer.CMDS_SET.keys()))
        item.combobox.currentIndexChanged.connect(
            lambda: self.slot_lstwdg_cmb_changed(self.listWidget__command.currentIndex()))

        self.listWidget__command.addItem(item)
        self.listWidget__command.setItemWidget(item, item.combobox)

    def slot_lstwdg_cmb_changed(self, index: QtCore.QModelIndex):
        if not index.isValid():
            return
        item: ComboBoxItem = self.listWidget__command.itemFromIndex(index)
        print(f'[changed combobox item] : {item.current_text}')

    def slot_del_item(self):
        idx = self.listWidget__command.currentIndex()
        if not idx.isValid():
            return
        item = self.listWidget__command.itemFromIndex(idx)
        btn: QtWidgets.QMessageBox.StandardButton = QtWidgets.QMessageBox.question(
            self, '실행 명령 제거', f'{item.text()} 명령을 제거할까요?')
        if btn == QtWidgets.QMessageBox.StandardButton.No:
            return
        self.listWidget__command.takeItem(idx.row())

    def slot_started_timer(self):
        self.listWidget__command.setEnabled(False)
        print('started!!')

    def slot_finished_timer(self):
        self.listWidget__command.setEnabled(True)
        print('finished!!')
        self.__init_set()

    @QtCore.Slot(Data)
    def slot_update_ui(self, data: Data):
        self.progressBar__remaining.setValue(data.ratio)
        self.lcdNumber__remaining.display(SingleTimer.secs2qtime(data.secs).toString())

        if data.secs <= 0:
            self.run_commands()

    def run_commands(self):
        cmds = self.get_commands()
        if not len(cmds):
            return
        for cmd in cmds:
            sys_lib.System.open_file_using_thread(pathlib.Path(SingleTimer.CMDS_SET.get(cmd)), None, False)

    def get_commands(self):
        cnt_items = self.listWidget__command.count()
        # Drag & Drop 사용할 때...
        # return [str(self.listWidget__command.item(i).text()) for i in range(cnt_items)]
        return [self.listWidget__command.item(i).current_text for i in range(cnt_items)]

    def slot_start_timer(self):
        if SingleTimer.qtime2secs(self.timeEdit__timer.time()) <= 0:
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

    def slot_stop_timer(self):
        if self.__work_thread.isRunning():
            self.__work_thread.stop()

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
    app = QtWidgets.QApplication(sys.argv)
    timer = SingleTimer()
    timer.show()
    sys.exit(app.exec_())
