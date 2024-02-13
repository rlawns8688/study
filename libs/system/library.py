#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.13
# modified date  :   2024.02.13
# description  :

import pathlib
from PySide2 import QtWidgets
import os
import re




class System:
    @staticmethod
    def get_files(pattern, parent_dir):
        for f in parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in pattern:
                yield f
            else:
                if f.suffix in pattern:
                    yield f

    @staticmethod
    def get_files_lst(pattern, parent_dir):
        lst = list()
        for f in parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in pattern:
                lst.append(f)
            else:
                if f.suffix in pattern:
                    lst.append(f)
        return lst

    @staticmethod
    def get_files_recursion(pattern, dpath, depth=0):
        lst = list()
        file_lst = os.listdir(dpath)
        for f in file_lst:
            # fullpath => '/home/rapa/workspace/usd/sdr/api.h'
            # fullpath => '/home/rapa/workspace/usd/sdr/testenv'
            fullpath = os.path.join(dpath, f)
            if os.path.isdir(fullpath):
                lst += System.get_files_recursion(pattern, fullpath, depth+1)
            else:
                if os.path.isfile(fullpath):
                    if '*' in pattern:
                        lst.append(fullpath)
                    else:
                        ext = f'.{fullpath.split(".")[-1]}'
                        if ext in pattern:
                            lst.append(fullpath)
        yield from lst




if __name__ == '__main__':
    pass
