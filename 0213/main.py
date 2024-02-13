#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.13
# modified date  :   2024.02.13
# description  :
import importlib
# 파일복사
# 소스 디렉토리
# 타켓 디렉토리
# 복사, 복사 중 정지, 복사 중 일시 정지(condition wait)
# 복사 완료된 파일 목록 리스트에 저장(mutex lock)
# SQLite3 DB (복사완료된 리스트 DB에 저장)
# 초기 실행 시, pause, stop 비활성화
    # start 클릭
        # pause 활성화
        # stop 활성화 변경
        # start 비활성화

    # stop 클릭
        # start 활성화
        # stop 비활성화
        # pause 비활성화

    # pause 클릭
        # start 활성화
        # stop 활성화
        # pause 비활성화

import sys
import pathlib
from PySide2 import QtWidgets, QtGui, QtCore
import resource.ui.costomFileCopy_ui as cus_file_cpy
import site
import shutil
import typing
import logging
import time
import os


site.addsitedir('/home/rapa/python/libs')
from qt import library as qt_lib
from system import library as sys_lib
from qt.library import LogHandler
importlib.reload(qt_lib)
importlib.reload(sys_lib)

# print(list(library.System.get_files_recursion('*','/home/rapa/python/')))

class MessageSig:
    message = ''
    is_err = False

class Signals(QtCore.QObject):
    progress_update = QtCore.Signal(int)
    message = QtCore.Signal(MessageSig)
    list_update = QtCore.Signal(str)


class UIThread(QtCore.QThread):
    def __init__(self, flst: typing.List[str], targetdir: str):
        super().__init__()
        self.signals = Signals()
        self.all_files = flst
        self.__targetdir = targetdir
        self.__is_stop = True
        self.__is_pause = False

    @property
    def itemlist(self):
        return self.itemlist
    @itemlist.setter
    def itemlist(self, val):
        self.itemlist = val

    def set_targetdir(self, val):
        self.__targetdir = val

    @property
    def is_stop(self):
        return self.__is_stop

    @is_stop.setter
    def is_stop(self, flag: bool):
        self.__is_stop = flag

    @property
    def is_pause(self):
        return self.__is_pause

    @is_pause.setter
    def is_pause(self, flag: bool):
        self.__is_pause = flag

    def run(self):

        for i, f in enumerate(self.all_files):
            ratio = int((i / (len(self.all_files) - 1)) * 100)
            dst_file = pathlib.Path(self.__targetdir) / pathlib.Path(f).name
            msg_sig = MessageSig()

            if not dst_file.exists():
                shutil.copy2(f, dst_file.as_posix())
                self.itemlist.append(dst_file.as_posix())
            else:
                msg_sig.message = f,f'{dst_file.as_posix()} 해당 파일이 존재합니다.'
                msg_sig.is_err = True

                self.signals.progress_update.emit(ratio)
                self.signals.message.emit(msg_sig)
                self.signals.list_update.emit(dst_file.as_posix())

                continue

            msg_sig.message = f'[{ratio}%] {f} -> {dst_file.as_posix()}'
            msg_sig.is_err = False

            # stop
            if self.__is_stop:
                break

            if self.__is_pause:
                while True:

                    time.sleep(0.2)
                    if not self.__is_pause:
                        break

            self.signals.progress_update.emit(ratio)
            self.signals.message.emit(msg_sig)







class CustomFileCopy(QtWidgets.QMainWindow, cus_file_cpy.Ui_MainWindow__filecopy):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # 초기 상태
        self.init_set()

        # variables
        self.__handler = qt_lib.LogHandler(out_stream=self.textBrowser__debug)
        self.__ui_thread = UIThread([], '')


        self.toolButton__srcdir.clicked.connect(self.slot_source_dir)
        self.toolButton__targetdir.clicked.connect(self.slot_source_dir)

        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__pause.clicked.connect(self.slot_pause)
        self.pushButton__stop.clicked.connect(self.slot_stop)
        self.__ui_thread.signals.progress_update.connect(self.slot_update_progress)
        self.__ui_thread.signals.message.connect(self.slot_print_message)
        self.__ui_thread.signals.list_update.connect(self.slot_listwidget)
    def init_set(self):
        self.toolButton__srcdir.setText('source directory')
        self.toolButton__targetdir.setText('target directory')
        self.pushButton__pause.setEnabled(False)
        self.pushButton__stop.setEnabled(False)


    @QtCore.Slot(MessageSig)
    def slot_print_message(self, msg: MessageSig):
        if msg.is_err:
            self.__handler.log_msg(logging.error, msg.message)
        else:
            self.__handler.log_msg(logging.info, msg.message)
    @QtCore.Slot(str)
    def slot_listwidget(self, val):
        self.listWidget.addItem(val)
    @QtCore.Slot(int)
    def slot_update_progress(self, val):
        self.progressBar.setValue(val)
    def get_all_files(self):
        dpath = self.lineEdit__srcdir.text()
        return list(sys_lib.System.get_files_recursion(['*'], dpath))
    def is_exists_target_dir(self):
        return QtCore.QDir(self.lineEdit__targetdir.text()).exists() and len(self.lineEdit__targetdir.text())

    def slot_start(self):
        self.pushButton__pause.setEnabled(True)
        self.pushButton__stop.setEnabled(True)
        self.pushButton__start.setEnabled(False)

        self.__ui_thread.is_pause = False

        if not self.__ui_thread.isRunning():
            self.__ui_thread.is_start = True
            self.__ui_thread.is_stop = False

        if not self.is_exists_target_dir():
            self.__handler.log_msg(logging.error, '타겟 디렉토리 설정을 해야합니다')
            return

        all_files = self.get_all_files()
        self.__ui_thread.all_files = all_files
        self.__ui_thread.set_targetdir(self.lineEdit__targetdir.text())

        if not len(all_files):
            self.__handler.log_msg(logging.error, '파일이 없습니다')
            return

        self.__ui_thread.start()
        self.__ui_thread.daemon = True


    def slot_stop(self):
        self.pushButton__pause.setEnabled(False)
        self.pushButton__stop.setEnabled(False)
        self.pushButton__start.setEnabled(True)


        self.__ui_thread.is_start = False
        self.__ui_thread.is_stop = True

    def slot_pause(self):
        self.pushButton__pause.setEnabled(False)
        self.pushButton__stop.setEnabled(True)
        self.pushButton__start.setEnabled(True)

        self.__ui_thread.is_pause = True
    def slot_source_dir(self):
        btn: QtWidgets.QToolButton = self.sender()
        sel_dir = qt_lib.QtLibs.dir_dialog('/home/rapa')

        if sel_dir is not None:
            if btn.text() == 'source directory':
                self.lineEdit__srcdir.setText(sel_dir.as_posix())
            else:
                self.lineEdit__targetdir.setText(sel_dir.as_posix())







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cfc = CustomFileCopy()
    cfc.show()
    sys.exit(app.exec_())
