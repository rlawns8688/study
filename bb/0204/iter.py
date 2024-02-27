# class MyIterator:
#     def __init__(self, data):
#         # index를 위한 변수
#         self.data = data
#         self.position = 0
#
#     def __iter__(self):
#         # next내장함수 호출
#         return self
#
#     def __next__(self):
#         # 인덱스는 0부터 시작하므로 이상이 0되면 예외 발생
#         if self.position >= len(self.data):
#             raise StopIteration
#         result = self.data[self.position]
#         self.position += 1
#         return result
#
#
# i = MyIterator([1, 2, 3, 4])
# for item in i:
#     print(item)
#
# def mygen():
#     for i in range(1, 1000):
#         result = i * i
#         yield result
import re


# number = '010-8688-7556'
# number2 = '+82 10-8688-7556'
# res = re.sub(r'\d-(.+)','010 - 8688 - 7556',number)
#
# print(res)


email_lst = [
'a34ds2aa@naver.com', ' edsa@gmail.com', '+#dsee@naver.com', 'xxse@gmail.com',
'eee22_slz@gmail.com', 'eeww@kakao.co.kr',
'a_z__bd43@naver.com'
]




def emialfilter(email_list):
    for i in email_list:
        comp = re.search(r'^[\w\d_]+@[\w\.]+\.[\w].+',i)
        print(comp)

    # print(comp)
    # for i in email_lst:
    #     res = comp.search(i)
    #     if res is None:
    #         continue
    #     yield(res)

emialfilter(email_lst)
# emialfilter(email_lst)
