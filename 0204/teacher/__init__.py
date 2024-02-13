#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.04
# modified date  :   2024.02.04
# description  :
from teacher.lib import findFiles, changeFiles
import pathlib
import os


if __name__ == '__main__':
    f = findFiles
    ff = f.FindFiles(
        pathlib.Path(''),
        ['.cpp', '.h'])
    c = changeFiles

    res = ff.get_files_recursion('/home/rapa/usd/sdr')
    cc = c.ChangeFiles('PXR2', '#include "PXR2', '#include "pxr(.+)')
    for i in res:
        assert isinstance(i, f.CheckWord)
        is_exist = f.CheckWord.is_check_word(i.fullpath, '#include "pxr')
        if is_exist is False:
            cc.change_file(pathlib.Path(i.fullpath), True)




