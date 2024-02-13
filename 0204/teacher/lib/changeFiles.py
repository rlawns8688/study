import pathlib
import random
import re


# 변경할 문자열, 찾을 문자열
# 해당 클래스에서 파일 변경

class ChangeFiles:
    def __init__(self, find_str: str, change_str: str, pattern: str):
        # 찾을 패턴
        self.__pattern = pattern
        # 검색 대상 문자열 (원본)
        self.__find_str = find_str
        # 바꿀 문자열
        self.__change_str = change_str

    def change_file(self, fpath: pathlib.Path, is_override=False) -> bool:
        try:
            with open(fpath.as_posix(), 'r') as fp:
                read = fp.read()
                self.__find_str = read

                changed_contents = re.sub(
                    r'{0}'.format(self.__pattern),
                    f'{self.__change_str}\g<1>',
                    self.__find_str)
            if is_override:
                with open(fpath.as_posix(), 'w') as fp:
                    fp.write(changed_contents)
                    return True
            else:
                with open(fpath.with_name(
                        '{0}.{1}'.format(fpath.name, random.randrange(1000))), 'w') as fp:

                    fp.write(changed_contents)
                    return True
        except (FileNotFoundError, IOError) as err:
            return False


if __name__ == '__main__':
    c = ChangeFiles('PXR2', '#include "PXR2', '#include "pxr(.+)')
    # c.change_file(pathlib.Path(testfile), True)
