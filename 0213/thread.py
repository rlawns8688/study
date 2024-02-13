#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.13
# modified date  :   2024.02.13
# description  :
import threading
import time

cnt = 0
class PrintClass(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.lock = threading.Lock()
        self.wait = threading.Condition()


    def run(self):
        global cnt

        for i in range(self.num):
            # time.sleep(0.5)
            # print(i)
            self.lock.acquire()
            self.wait.wait(self.lock)
            self.wait.wait(5)
            cnt += 1
            self.lock.release()

# def print_func(num):
#     for i in range(num):
#         print(i)

# th = threading.Thread(target=print_func,args=(5,), daemon=True)
# th2 = threading.Thread(target=print_func,args=(3,), daemon=True)

th = PrintClass(4)
th2 = PrintClass(5)
print(cnt)
th.run()
th2.run()
th.setDaemon = True
th2.setDaemon = True

# th.start()
# th2.start()

# th.join()
# th2.join()



if __name__ == '__main__':
    pass
