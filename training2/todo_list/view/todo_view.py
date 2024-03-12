#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.02
# modified date : 2024.03.02
# description   :

from PySide2 import QtWidgets, QtGui


class TodoView(QtWidgets.QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.alternatingRowColors()
        _font = QtGui.QFont('FiraCodeRetina', 18)
        self.setFont(_font)


if __name__ == '__main__':
    pass
