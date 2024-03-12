#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.03
# modified date : 2024.03.03
# description   :

import sys

import pytest

sys.path.insert(0, '/home/rapa/workspace/python/training2')

from todo_list.lib import db


def test_add_todo():
    # ('home tra', '2023/12/15', '2023/12/31', 2, 3);

    db_todo = db.DBTodolist()
    res = db_todo.add_todo(('coding test practice', '2023/12/15', '2023/12/31', 2, 7))
    assert res == True


@pytest.mark.skip
def test_del_todo():
    db_todo = db.DBTodolist()
    res = db_todo.del_todo(4)
    assert res == True


def test_update_todo():
    db_todo = db.DBTodolist()
    res = db_todo.update_todo(8, 1)
    assert res == True


if __name__ == '__main__':
    pass
