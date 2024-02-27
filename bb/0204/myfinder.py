#pxr -> PXR
import pathlib
import re
import os
class PXR():
    def __init__(self, pxrpath):
        self.__pxrpath = pxrpath

    @property
    def pxrpath(self):
        return self.__pxrpath

    @pxrpath.setter
    def pxrpath(self, val):
        self.__pxrpath = val
    def find(self):
        lst = []
        get_path = pathlib.Path(self.pxrpath)
        path = get_path.glob('**/*.cpp')
        for i in get_path.glob('**/*.cpp'):
            # i 는 cpp파일의 경로
            with open(i,'r') as fp:
                # line 은 cpp 파일 안의 한 문장
                for line in fp.readlines():
                    line.strip('\n')
                    res = re.search('pxr', line)
                    # pxr이 포함된 문장이 있으면 그 파일의 경로를 lst에 추가
                    if res is not None:
                        # Posix어쩌구 빼고 경로만
                        r = i.as_posix()
                        #중복해서 저장 안하게
                        if r not in lst:
                            lst.append(r)

        # 모든 pxr단어를 지닌 파일들의 경로 리스트를 반환
        # print(lst)
        return lst

    def change(self):
        pxrpath_lst = self.find()
        for pxrpath in pxrpath_lst:
            with open(pxrpath, 'r') as fp:
                lines = fp.read()
                print(lines)
            with open(pxrpath, 'w') as fp:
                res = re.sub('pxr', 'PXR', lines)
                fp.write(res)
                print(res)



a = PXR('/home/rapa/usd/ndr')
# a.find()
a.change()