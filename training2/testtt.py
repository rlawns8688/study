#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.02
# modified date : 2024.03.02
# description   :

from PySide2 import QtWidgets, QtGui, QtCore


def label_widget():
    label_w = QtWidgets.QLabel('test string!!')
    font = QtGui.QFont('', 20)
    label_w.setFont(font)
    label_w.setFixedSize(500, 500)
    label_w.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight) #

    print(int(QtCore.Qt.AlignRight))    # 0000 0010
    print(int(QtCore.Qt.AlignTop))      # 0010 0000

    print(int(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight))      # 0010 0000

    return label_w


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    label = label_widget()
    label.show()
    app.exec_()


