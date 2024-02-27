#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.17
# modified date  :   2024.02.17
# description  :   



from pydantic import BaseModel

class Data(BaseModel):
    a: int
    b: float
    c: str

class Main:
    def __init__(self):
        self.data = Data(a=1, b=1.5, c=1)



if __name__ == '__main__':
    m = Main()
    print(m.data)
