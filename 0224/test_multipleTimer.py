#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.24
# modified date  :   2024.02.24
# description  :
import pathlib

import pytest
import sys


sys.path.append('/home/rapa/study/0224/resources')
import multipleTimer


def test_get_time2seconds():
    # mt = multipleTimer.MutipleTimer()
    qtime = multipleTimer.MutipleTimer.secs2qtime(1000)
    sec = multipleTimer.MutipleTimer.qtime2secs(qtime)
    assert sec == 1000

def test_addition():
    assert multipleTimer.MutipleTimer.addition(3, 5) == 8

def test_open_file_using_thread():
    # import hou
    import sys
    sys.path.insert(0,'/home/rapa/study/libs/system')
    sys_lib = pytest.importorskip(modname='library')

    assert sys_lib.System.open_file_using_thread(pathlib.Path('/usr/bin/gnome-terminal'), None, False) == True



if __name__ == '__main__':
    pass
