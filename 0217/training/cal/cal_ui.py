#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.17
# modified date  :   2024.02.17
# description  :   
import sys
from PySide2 import QtWidgets, QtGui, QtCore


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
        for i in range(10):
            btn = QtWidgets.QPushButton(str(i))
            btn.clicked.connect(self.slot_clicked_btn)
            self.grid_layout.addWidget(btn, int(i // 3), int(i % 3))

            if i == 9:
                value = 'C'
            elif i == 10:
                value = '.'
            # for i in range(9):
            # # if i == 0:
            # #     value = 'C'
            # # elif i == 1:
            # #     value = '.'
            # # else:
            # #     value = i
            #
            # btn = QtWidgets.QPushButton(str(i))
            # btn.clicked.connect(self.slot_clicked_btn)
            # self.grid_layout.addWidget(btn, int((8 - i) // 3), int((8 - i) % 3))

    def slot_clicked_btn(self):
        # print(self.sender().text())
        data: QtWidgets.QPushButton = self.sender()
        res = self.line_edit.text().strip()
        self.line_edit.setText(res + data.text())



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    pass
