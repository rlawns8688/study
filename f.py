import shutil
import pathlib
import pprint
import re
dirpath = pathlib.Path("/home/rapa/python/seqeunce_data")

res = dirpath.glob("*.exr")

comp =re.compile(r'\.(?P<frange>[0-9]{4})\.', re.DOTALL)
file_framge_lst = list()
for i in res:
    srch = comp.search(i.name)
    file_framge_lst.append(srch.group('frange'))


lst = range(1001,1151)
print(list(lst))
frame_info = set(lst) ^ set(file_framge_lst)
s = 'render.1145.exr'
zz = re.search(r'.([0-9]{4})\.',s, re.DOTALL)
print(list(frame_info))