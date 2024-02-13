import sys
import importlib
from PySide2 import QtWidgets, QtGui, QtCore
import os
import pyseq
import hou
from resource.ui import Sequence_Manager_ui
importlib.reload(Sequence_Manager_ui)



class SequenceManager(QtWidgets.QMainWindow, Sequence_Manager_ui.Ui_mainWindow__seq):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setupUi(self)
            self.listWidget_missing.addItems(['qaaaa','bb','cc'])

            self.listWidget_missing.customContextMenuRequested.connect(self.custom_context)

            self.listWidget_missing.currentItemChanged.connect(self.changed_missing_item)

            self.toolButton_dirpath.clicked.connect(self.select_directory)

        def changed_missing_item(self,idx: QtWidgets.QListWidgetItem):
            print(idx.text)

        def custom_context(self, pos: QtCore.QPoint):
            print(pos.x())

        def select_directory(self):
            file_dialog = QtWidgets.QFileDialog()
            directory = file_dialog.getExistingDirectory(self, "폴더 선택")
            self.lineEdit_dirpath.setText(directory)
            # print(directory)  # 선택된 폴더 경로를 출력합니다.
            files_in_directory = os.listdir(directory)
            sortlist = sorted(files_in_directory)
            # print(sortlist)
            listname = list
            s1 = sortlist[0]
            s2 = sortlist[-1]
            a = [s1,s2]
            self.listWidget.addItem(str(a))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    seq_mgr = SequenceManager()
    seq_mgr.show()
    sys.exit(app.exec_())
