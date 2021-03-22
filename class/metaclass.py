class HogeMetaClass(type):
    def __new__(cls, name, base, dct):
        print("dict: " + str(dct))
        return super().__new__(cls, name, base, dct)

class Hoge(object, metaclass=HogeMetaClass):
    pass

class Sample(Hoge):
    _test = 0

    def hoge(self):
        return "hoge"

if __name__ == '__main__':
    print("begin")
    sample = Sample()
    print("_test: " + str(sample._test))
    print("self.hoge: " + str(sample.hoge()))
