import pathlib
import sys
import re

#Q1) 회문 검출 함수
class Check:
    def __init__(self):
        self.__path = pathlib.Path('/home/rapa/python/0130/123.txt')

    def load_file(self):
        words = list()
        count = dict()
        with open(self.__path, 'rt') as fp:
            for lines in fp.readlines():
                a = lines.strip('\n')
                words.extend(a.split(' '))
                for word in words:
                    if word not in count:
                        count[word] = 1
                    else:
                        count[word] += 1
            return count

    def get_words(self):
        rev_dict = []
        words = self.load_file()
        for k,v in words.items():
            rev = k[::-1]
            if k == rev and len(k) != 1:
                print(k, ':', v)

c = Check()
c.get_words()













# Q2) 버블 정렬
l1 = [3, 4, 5, 6, 1, 32, 7]

class BubbleSort:
    def sort(self, lst):
        n = len(lst)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

        return lst

def callback(a,b):
    return a > b



# class 사용해서
#이중 for문
# print(l1[1] > l1[0])

# l1[1] > l1[4]

b = BubbleSort()
print(b.sort([3.4, 3, 6, 2, 1, 8, 43, 5]))






