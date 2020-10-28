# 参考
# https://qiita.com/tchnkmr/items/e740173d7400f8672d75

class MyIterSample(object):
    def __init__(self):
        self.__item = []

    def add(self, item):
        self.__item.append(item)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if len(self.__item) <= self.__index:
            raise StopIteration()

        ret = self.__item[self.__index]
        self.__index += 1
        return ret
