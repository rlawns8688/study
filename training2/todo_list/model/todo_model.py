#!/usr/bin/env python
# encoding=utf-8
import datetime

# author        : seongcheol jeon
# created date  : 2024.03.02
# modified date : 2024.03.02
# description   :
import libs.utility.utils as utils
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtGui import QColor
from todo_list.main import TodoStatus, TodoItem


class TodoModel(QtCore.QAbstractListModel):
    id_role = QtCore.Qt.UserRole + 1
    test_role = QtCore.Qt.UserRole + 2

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
        # print(self.__data)
        if role == QtCore.Qt.DisplayRole:
            todo_item: TodoItem = self.__data[index.row()]
            return todo_item.todo

        elif role == QtCore.Qt.TextColorRole:
            todo_item: TodoItem = self.__data[index.row()]
            ste: str = todo_item.todo_status
            if ste == "complete":
                return QtGui.QColor(255, 0, 0, 255)
            return QtGui.QColor()

        elif role == QtCore.Qt.ToolTipRole:
            cdate: datetime.datetime = self.__data[index.row()].deadline
            return f'deadline: {cdate.strftime("%Y-%m-%d %H:%M:%S")}'

        elif role == QtCore.Qt.BackgroundRole:
            # todo_item: TodoItem = self.__data[index.row()]
            now = datetime.datetime.now()
            # deadline = todo_item.deadline
            deadline = datetime.datetime.fromisoformat("2025-03-24 15:10")
            delta = deadline - now
            ratio = utils.fit(delta.seconds, 0, 500, 0, 1)
            print(ratio)
            return QtGui.QColor(int(ratio * 255),0 ,0 ,255)

            # 마감 기한과 현재 날짜의 차이를 기준으로 색상 정규화
            # if delta < 0:
            #     # 이미 마감 기한이 지난 경우
            #     color = QtGui.QColor(255, 0, 0, 100)  # 어두운 빨간색
            # else:
            #     # 정규화 과정: 0일 <= delta <= 7일을 0 <= intensity <= 255로 매핑
            #     max_days = 7
            #     intensity = max(0, 255 - int((delta / max_days) * 255))
            #     color = QtGui.QColor(255, 255 - intensity, 255 - intensity, 100)
            #
            # return QtGui.QBrush(color)



        elif role == TodoModel.id_role:
            return self.__data[index.row()].data_id

        elif role == TodoModel.test_role:
            return "test role!!!"

    def rowCount(self, parent=...):
        return len(self.__data)


if __name__ == "__main__":
    pass
