import pathlib
import random
import re


# 변경할 문자열, 찾을 문자열
# 해당 클래스에서 파일 변경

# 파일 내용을 변경하여 저장하는 클래스
class ChangeFiles:
    def __init__(self, change_str: str, pattern: str):
        '''
        :param change_str: 바꿀 문자열
        :param pattern: 찾을 패턴
        '''
        self.__pattern = pattern
        self.__change_str = change_str

    # 파일 내용 변경 메서드
    def change_file(self, fpath: pathlib.Path, is_override=False) -> bool:
        '''
        :param fpath: 읽어 들일 파일 경로
        :param is_override: 원본을 덮어쓸지
        :return: 변경 완료가 잘 되었다면 참
        '''
        try:
            # 파일 열기 - 변경을 위한
            with open(fpath.as_posix(), 'r') as fp:
                read = fp.read()

                # 파일 내용 변경
                changed_contents = re.sub(
                    r'{0}'.format(self.__pattern), f'{self.__change_str}\g<1>', read)
            # 만약 원본 덮어쓰기라면
            if is_override:
                with open(fpath.as_posix(), 'w') as fp:
                    fp.write(changed_contents)
                    # 잘 저장되었다고 true 전달
                    return True
            # 그렇지 않다면, 다른 이름으로 저장
            else:
                # 임의의 다른 이름으로 저장
                # ex) /home/rapa/aaa.cpp    ->      /home/rapa/aaa.cpp.55
                with open(fpath.with_name(
                        '{0}.{1}'.format(fpath.name, random.randrange(1000))), 'w') as fp:
                    fp.write(changed_contents)
                    # 잘 저장되었다고 true 전달
                    return True
        # FileNotFoundError, IOError 예외 발생 시
        except (FileNotFoundError, IOError) as err:
            # 변경 저장 실패했다고 false 전달
            return False


if __name__ == '__main__':
    c = ChangeFiles('#include "PXR2', '#include "pxr(.+)')
    # c.change_file(pathlib.Path(testfile), True)
