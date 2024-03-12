#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.02
# modified date : 2024.03.02
# description   :

from PySide2 import QtWidgets, QtGui, QtCore

from training2.todo_list.main import TodoStatus, TodoItem


class TodoModel(QtCore.QAbstractListModel):
    id_role = QtCore.Qt.UserRole + 1

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.__data: list = data

    def get_data(self):
        return self.__data

    def add_data(self, data):
        self.__data.append(data)
        self.layoutChanged.emit()

    def del_data(self, row):
        del self.__data[row]
        self.layoutChanged.emit()

    def update_status(self, row, ste):
        self.__data[row].todo_status = ste
        self.dataChanged.emit(self.index, self.index)

    def data(self, index, role=...):
        if role == QtCore.Qt.DisplayRole:
            todo_item: TodoItem = self.__data[index.row()]
            return todo_item.todo

        elif role == QtCore.Qt.TextColorRole:
            todo_item: TodoItem = self.__data[index.row()]
            ste: str = todo_item.todo_status
            if ste == "complete":
                return QtGui.QColor(255, 0, 0, 255)
            return QtGui.QColor()

        elif role == TodoModel.id_role:
            # (1, 'todo string', datetime, datetime, 'waiting', 2),
            return self.__data[index.row()].data_id

    def rowCount(self, parent=...):
        return len(self.__data)


if __name__ == "__main__":
    pass