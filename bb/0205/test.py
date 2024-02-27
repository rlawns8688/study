#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.05
# modified date  :   2024.02.05
# description  :   

# Q1
a = 'a:b:c:d'
b = a.split(':')
c = '#'.join(b)
print(c)

# Q2
a = {'A': 90, 'B': 80}
a['C'] = 70
print(a)

# Q3
a = [1, 2, 3]
print(id(a))
a = a + [4, 5]
print(id(a))
b = [1, 2, 3]
print(id(b))
b.extend([4, 5])
print(id(b))
# extend는 id를 유지한다


# Q4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in range(len(A)):
    if A[i] >= 50:
        sum += A[i]
print(sum)



# Q5
def fibonacci_list(n):
    fib_list = [0, 1]  # 첫 번째 항과 두 번째 항을 리스트에 미리 저장합니다.
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])  # 이전 두 항을 더한 값을 리스트에 추가합니다.
    return fib_list

print(fibonacci_list(10))



# Q6
def count(*nums):
    numlst = list(nums)
    sum = 0
    for i in range(len(numlst)):
        sum += numlst[i]
    print(sum)

count(65,45,2,3,45,8)


# Q7
with open('/home/rapa/python/0205/abc.txt', 'r') as fp:
    lines = fp.readlines()
    reverselines = reversed(lines)
    for line in reverselines:
        line = line.strip('\n')
        print(line)
with open('/home/rapa/python/0205/abc.txt', 'w') as fp:
    fp.writelines(line)












if __name__ == '__main__':
    pass
