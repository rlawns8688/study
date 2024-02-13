import os
import re
import pathlib


# 부모 디렉토리
# 특정 확장자만 찾을 수 있는 옵션


class CheckWord:
    def __init__(self, fpath: str, depth: int):
        self.__fpath = fpath
        self.__depth = depth

    @property
    def fullpath(self) -> pathlib.Path:
        return pathlib.Path(self.__fpath)

    @property
    def depth(self) -> int:
        return self.__depth

    @staticmethod
    def is_check_word(fpath: pathlib.Path, find_str: str) -> bool:
        comp = re.compile(r'{0}'.format(find_str))
        with fpath.open('r') as fp:
            return comp.search(fp.read()) is not None

class FindFiles:
    def __init__(self,
                 parent_dir: pathlib.Path,
                 pattern: list):
        self.__parent_dir = parent_dir
        self.__pattern = pattern

    @property
    def parent_dir(self) -> pathlib.Path:
        return self.__parent_dir

    @property
    def pattern(self) -> list:
        return self.__pattern

    def get_files(self):
        for f in self.parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in self.pattern:
                yield f
            else:
                if f.suffix in self.pattern:
                    yield f

    def get_files_lst(self):
        lst = list()
        for f in self.parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in self.pattern:
                lst.append(f)
            else:
                if f.suffix in self.pattern:
                    lst.append(f)
        return lst

    def get_files_recursion(self, dpath, depth=0):
        lst = list()
        file_lst = os.listdir(dpath)
        for f in file_lst:
            # fullpath => '/home/rapa/workspace/usd/sdr/api.h'
            # fullpath => '/home/rapa/workspace/usd/sdr/testenv'
            fullpath = os.path.join(dpath, f)
            if os.path.isdir(fullpath):
                lst += self.get_files_recursion(fullpath, depth+1)
            else:
                if os.path.isfile(fullpath):
                    if '*' in self.pattern:
                        lst.append(CheckWord(fullpath, depth))
                    else:
                        ext = f'.{fullpath.split(".")[-1]}'
                        if ext in self.pattern:
                            lst.append(CheckWord(fullpath, 0))
        yield from lst


if __name__ == '__main__':
    ff = FindFiles(
        pathlib.Path('/home/rapa/workspace/usd/sdr'),
        ['.cpp', '.h'])
    # print(list(ff.get_files()))
    # print(ff.get_files_lst())

    res = ff.get_files_recursion('/home/rapa/workspace/usd/sdr')
    for i in res:
        assert isinstance(i, CheckWord)
        is_exist = CheckWord.is_check_word(i.fullpath, '#include "pxr')
        print(
            f'{i.fullpath} - {i.depth}: {is_exist}')
