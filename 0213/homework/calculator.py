import sys
# import time
# import pathlib
import importlib

import keyPressCal_ui

from PySide2 import QtWidgets, QtGui, QtCore

importlib.reload(keyPressCal_ui)


#todo : set_ui_btn 에서 생성하는거 10,11 대신에 enter,cancel로 바꾸기
class Calculator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.grid_layout = QtWidgets.QGridLayout()
        self.line_edit = QtWidgets.QLineEdit()

        self.set_ui_btn()

        self.vlayout.addWidget(self.line_edit)
        self.vlayout.addLayout(self.grid_layout)

        self.setLayout(self.vlayout)

    def set_ui_lnedit(self):
        pass

    def set_ui_btn(self):
        lst = ['+', '-', '*', '//']

        for i in range(16):
            if i == 14:
                btn = QtWidgets.QPushButton('Enter')
            elif i == 15:
                btn = QtWidgets.QPushButton('Cancel')
            elif i < len(lst):
                btn = QtWidgets.QPushButton(lst[i])
            else:
                btn = QtWidgets.QPushButton(str(i - len(lst)))

            btn.clicked.connect(self.slot_clicked_btn)
            self.grid_layout.addWidget(btn, int(i // 4), int(i % 4))

    def slot_clicked_btn(self):
        # print(self.sender().text())
        data: QtWidgets.QPushButton = self.sender()
        if self.sender().text() == 'enter':

        res = self.line_edit.text().strip()
        self.line_edit.setText(res + data.text())

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
            try:
                result = eval(self.line_edit.text())
                self.line_edit.setText(str(result))
            except Exception as e:
                print("계산 오류:", e)

            key_text = event.text()
            if key_text.isdigit():
                self.line_edit.setText(self.lineEdit.text() + key_text)
            elif key_text == '+':
                self.line_edit.setText(self.lineEdit.text() + '+')
            elif key_text == '-':
                self.line_edit.setText(self.lineEdit.text() + '-')
            elif key_text == '/':
                self.line_edit.setText(self.lineEdit.text() + '/')
            elif key_text == '*':
                self.line_edit.setText(self.lineEdit.text() + '*')



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    pass
