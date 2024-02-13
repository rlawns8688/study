#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.04
# modified date : 2024.02.04
# description   :

import sys
import time
# import threading
import pathlib
import importlib
import logging

from lib import changeFiles, findFiles
from resource.ui import change_keyword_ui

from PySide2 import QtWidgets, QtGui, QtCore

importlib.reload(change_keyword_ui)

logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] : %(message)s',
    level=logging.DEBUG,
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


class Info:
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    @property
    def arguments(self):
        return self.__args

    @arguments.setter
    def arguments(self, args: tuple):
        self.__args = args

    @property
    def keyword_args(self):
        return self.__kwargs

    @keyword_args.setter
    def keyword_args(self, kwargs: dict):
        self.__kwargs = kwargs


class CustomSignal(QtCore.QObject):
    signal_info = QtCore.Signal(Info)


class WorkThread(QtCore.QThread):
    def __init__(self, files, fstr, inst_cf):
        super().__init__()
        self.custom_sig = CustomSignal()

        self.flst = list(files)
        self.fstr = fstr
        self.cf = inst_cf

        self.is_stop = False

    def set_files(self, f):
        self.flst = list(f)

    def run(self):
        for i, f in enumerate(self.flst):
            assert isinstance(f, findFiles.CheckWord)
            assert isinstance(i, int)
            ratio = int((i / (len(self.flst) - 1)) * 100)

            is_exist = findFiles.CheckWord.is_check_word(
                f.fullpath, self.fstr)

            if not is_exist:
                continue

            is_suc = self.cf.change_file(f.fullpath)

            data = {
                'is_suc': is_suc,
                'ratio': ratio,
                'file_path': f.fullpath.as_posix()
            }

            self.custom_sig.signal_info.emit(Info(**data))

            time.sleep(0.1)


class ChangeFilesUI(QtWidgets.QMainWindow, change_keyword_ui.Ui_MainWindow__change_keyword):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.progressBar.setValue(0)

        self.__work_thread = WorkThread('', '', '')
        self.__ext_flst = list()

        # self.__work_thread.start()

#################
        # change_str: str, pattern: str,
        # parent_dir: pathlib.Path, ext_pattern: list):
        self.__cf = changeFiles.ChangeFiles('', '')
        self.__ff = findFiles.FindFiles(pathlib.Path(), [])
#################

        self.toolButton__pdir.clicked.connect(self.slot_pdir)
        self.lineEdit__file_ext.returnPressed.connect(self.slot_ext_flst)
        self.pushButton__start.clicked.connect(self.slot_progressbar)
        self.pushButton__stop.clicked.connect(self.slot_stop_progress)

        self.__work_thread.custom_sig.signal_info.connect(self.slot_info)

        ####### test code ###########
        self.__test_set_parms()
        ####### test code ###########


    @QtCore.Slot(Info)
    def slot_info(self, info: Info):
        self.progressBar.setValue(info.keyword_args.get('ratio'))
        srcfile = info.keyword_args.get('file_path')
        self.textEdit__log.append(srcfile)

    def slot_stop_progress(self):
        if self.__work_thread.isRunning():
            self.__work_thread.is_stop = True

    @QtCore.Slot(bool)
    def slot_finished_work(self, flag):
        if self.__work_thread.isFinished():
        # if flag:
            # self.__work_thread.stop()
            self.textEdit__log.append('finided work')
            logging.debug('debug logging')
        else:
            pass
            # print('progressing')

    def slot_progressbar(self):
        self.progressBar.setValue(0)
        if not self.__work_thread.isRunning():
            # change_str = '#include "PXR2'
            change_str = self.lineEdit__change_str.text()
            # pattern = f'{find_str}(.+)'
            pattern = self.lineEdit__find_pattern.text()
            parent_dir = pathlib.Path(self.lineEdit__pdir.text())
            ext_pattern = self.slot_ext_flst()

            self.__cf.pattern = pattern
            self.__cf.change_str = change_str
            self.__ff.parent_dir = parent_dir
            self.__ff.pattern = ext_pattern

            files = self.__ff.get_files_recursion(parent_dir)

            self.__work_thread.set_files(files)
            self.__work_thread.fstr = pattern.replace('(.+)', '')
            self.__work_thread.cf = self.__cf

            # dd = (list(files))
            # print(dd)
            # print(dd[0].fullpath)

            self.__work_thread.start()
        else:
            self.textEdit__log.append('이미 실행중...')
            logging.debug('run... logging')

    def slot_pdir(self):
        dpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, caption='asdd', dir='/data', )
        if not len(dpath):
            return
        dpath = pathlib.Path(dpath)
        self.lineEdit__pdir.setText(dpath.as_posix())

    def slot_ext_flst(self):
        text = self.lineEdit__file_ext.text()
        if not len(text):
            self.__ext_flst = list()
            return
        self.__ext_flst = list(map(lambda x: x.strip(), text.split()))
        return self.__ext_flst

    def __test_set_parms(self):
        self.lineEdit__pdir.setText('/home/rapa/workspace/usd/usdUI')
        self.lineEdit__file_ext.setText('.cpp .h')
        self.lineEdit__change_str.setText('#include "PXR2')
        self.lineEdit__find_pattern.setText('#include "pxr(.+)')


if __name__ == '__main__':
    # find_str = '#include "pxr'
    # main = Main(
    #     change_str='#include "PXR2',
    #     pattern=f'{find_str}(.+)',
    #     parent_dir=pathlib.Path('/home/rapa/workspace/usd/usdUI'),
    #     ext_pattern=['.cpp', '.h']
    # )

    # main.change_contents(find_str)

    app = QtWidgets.QApplication(sys.argv)
    ui = ChangeFilesUI()
    ui.show()
    sys.exit(app.exec_())


