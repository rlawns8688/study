#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.24
# modified date : 2024.02.24
# description   :

import pytest

from PySide2 import QtWidgets, QtGui, QtCore

import pathlib
import sys

sys.path.append('/home/rapa/workspace/python/training/timer')
import multipleTimer


# @pytest.mark.skip
def test_get_time2seconds():
    # mt = multipleTimer.MultipleTimer()
    qtime = multipleTimer.MultipleTimer.secs2qtime(1000)
    sec = multipleTimer.MultipleTimer.qtime2secs(qtime)
    assert sec == 1000


def test_addition():
    assert multipleTimer.MultipleTimer.addition('3', '5') == '35'


def test_open_file_using_thread():
    # import hou
    import sys
    sys.path.insert(0, '/home/rapa/workspace/python/libraries/system')
    sys_lib = pytest.importorskip(modname='library')

    assert sys_lib.System.open_file_using_thread(pathlib.Path('/usr/bin/gnome-terminal'), None, False) == True