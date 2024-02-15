import sys
# import time
# import pathlib
import importlib

import keyPressCal_ui

from PySide2 import QtWidgets, QtGui, QtCore

importlib.reload(keyPressCal_ui)



class PressKeyCalUI(QtWidgets.QMainWindow, keyPressCal_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)



        # self.toolButton__pdir.clicked.connect(self.slot_pdir)

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
            try:
                result = eval(self.lineEdit.text())
                self.lineEdit.setText(str(result))
            except Exception as e:
                print("계산 오류:", e)
        else:
            key_text = event.text()
            if key_text.isdigit():
                self.lineEdit.setText(self.lineEdit.text() + key_text)
            elif key_text == '+':
                self.lineEdit.setText(self.lineEdit.text() + '+')
            elif key_text == '-':
                self.lineEdit.setText(self.lineEdit.text() + '-')
            elif key_text == '/':
                self.lineEdit.setText(self.lineEdit.text() + '/')
            elif key_text == '*':
                self.lineEdit.setText(self.lineEdit.text() + '*')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = PressKeyCalUI()
    ui.show()
    sys.exit(app.exec_())

