# #Q1
# i = 2
# mul = 72
# while i<mul:
#     gugu = i%10
#     dan = i//10+2
#     if gugu != 0 and gugu !=1 and dan%2 ==1:
#         print('{0} x {1} = {2}'.format(dan,gugu,gugu*dan))
#     i += 1

#Q2
# def recursive_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + recursive_sum(n-1)
#
# result = recursive_sum(100)
# print(result)

# def re_add(res, idx):
#     if idx > 100:
#         return res
#     res += idx
#     idx += 1
#     return re_add(res, idx)
#
# result = re_add(0, 1)
# print(f'재귀함수 1~100까지 더한 값 : {result}')