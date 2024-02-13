import sys
import shutil
import pathlib
import importlib

import pyseq
from PySide2 import QtWidgets, QtGui, QtCore

# sys.path.append('/home/rapae/python/sequence_manager/resource/rc')

from resource.ui import Sequence_Manager_ui
importlib.reload(Sequence_Manager_ui)


class SequenceManager(QtWidgets.QMainWindow, Sequence_Manager_ui.Ui_mainWindow__seq):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)

        # variables
        #

        # self.listWidget__seq_info.addItems(['a', 'b', 'c'])
        # self.listWidget__missing.addItems(['aaaaaa', 'bbbbbb', 'ccccccc'])

        self.listWidget.customContextMenuRequested.connect(self.custom_context_seq_info)

        self.listWidget_missing.currentItemChanged.connect(self.changed_missing_item)
        # button
        self.toolButton_dirpath.clicked.connect(self.slot_select_dirpath)

    def slot_select_dirpath(self):
        dpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, caption='asdd', dir='/data')
        if not len(dpath):
            return
        dpath = pathlib.Path(dpath)
        self.lineEdit_dirpath.setText(dpath.as_posix())
        self.set_seq_file_info()

    def set_seq_file_info(self):
        seq_dpath = pathlib.Path(self.lineEdit_dirpath.text())
        print(seq_dpath.exists())
        file_gen = seq_dpath.glob('*.exr')
        file_names = list(map(lambda x: x.name, file_gen))
        chunk_file_info = pyseq.Sequence(file_names)

        self.listWidget.addItem(str(chunk_file_info))

    def changed_missing_item(self, idx: QtWidgets.QListWidgetItem):
        print(idx.text())

    def custom_context_seq_info(self, pos: QtCore.QPoint):
        index = self.listWidget_seq_info.indexAt(pos)
        if not index.isValid():
            return
        context = QtWidgets.QMenu(self)
        test_menu = QtWidgets.QMenu('Info', self)

        action_test_menu_seq_info = QtWidgets.QAction('detail', self)
        test_menu.addAction(action_test_menu_seq_info)

        action_seq_info = QtWidgets.QAction('시퀀스 정보', self)
        context.addAction(action_seq_info)
        context.addMenu(test_menu)

        actions = context.exec_(self.listWidget__seq_info.mapToGlobal(pos))

        if actions == action_test_menu_seq_info:
            print('acccccccccccccccccccc111')

        print(index.data())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    seq_mgr = SequenceManager()
    seq_mgr.show()
    sys.exit(app.exec_())