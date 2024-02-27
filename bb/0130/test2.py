class OpenFile:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.__fp = None

    # __enter__() with문에 딱 들어갔을 때 실행 되는 함수
    def __enter__(self):
        self.__fp = open(self.__filepath)
        print('파일 열렸다!')
        return self.__fp

    # __exit__ with문 실행 끝나고 나갔을 때 실행. 즉, 자동으로 close() 되는 with문의 특성을 우리가 구현할 수 있음.
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()

class CheckWord:
    def __init__(self):
        pass

    # 회문인지 체크하는 메서드
    def is_word(self, word):
        lst = list()
        for i in range(len(word) // 2):
            lst.append(word[i] == word[-1 - i])
        return all(lst) # 하나라도 거짓이면 안됨. any()는 하나라도 참이면 참!

    def word_list(self):
        with OpenFile('/data/test.txt') as fp: #fliter를 2단어 이하는 걸러보자!
            return filter(lambda x: len(x) > 2, fp.read().split())

    def get_word(self) -> dict:
        d = dict()
        for word in self.word_list():
            if self.is_word(word): # 회문이면 dict에 넣어줌.
                if word in list(d.keys()):
                    d[word] += 1
                else:
                    d[word] = 1
        return d


cw = CheckWord()
print(cw.get_word())