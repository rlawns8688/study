#!/usr/bin/env python
# encoding=utf-8

# author        : kim jun hyuk
# created date  : 2024.02.04
# modified date : 2024.02.04
# description   :

import sys
import pathlib

from lib import changeFiles, findFiles


class Main:
    def __init__(
            self,
            find_str: str, change_str: str, pattern: str,
            parent_dir: pathlib.Path, ext_pattern: list):
        self.__cf = changeFiles.ChangeFiles(find_str, change_str, pattern)
        self.__ff = findFiles.FindFiles(parent_dir, ext_pattern)
        self.__parent_dir = parent_dir

    def change_contents(self):
        files = self.__ff.get_files_recursion(self.__parent_dir)
        for i in files:
            assert isinstance(i, findFiles.CheckWord)
            is_exist = findFiles.CheckWord.is_check_word(
                i.fullpath, '#include "pxr')
            if not is_exist:
                continue
            is_suc = self.__cf.change_file(i.fullpath)
            if not is_suc:
                sys.stderr.write(f'{i.fullpath.as_posix()}: 에러 발생!')


if __name__ == '__main__':
    main = Main(
        find_str='PXR2', change_str='#include "PXR2',
        pattern='#include "pxr(.+)',
        parent_dir=pathlib.Path('/home/rapa/workspace/usd/sdr'),
        ext_pattern=['.cpp', '.h']
    )

    main.change_contents()