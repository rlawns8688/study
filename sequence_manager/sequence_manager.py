
import sys
import importlib

from PySide2 import QtWidgets, QtGui, QtCore

sys.path.append('/home/rapa/workspace/python/sequence_manager/resource/rc')

from resource.ui import sequence_manager_ui
importlib.reload(sequence_manager_ui)


class SequenceManager(QtWidgets.QMainWindow, sequence_manager_ui.Ui_MainWindow__seq_mgr):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    seq_mgr = SequenceManager()
    seq_mgr.show()
    sys.exit(app.exec_())