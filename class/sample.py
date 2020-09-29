class Animal:
    def __init__(self, a):
        self.__nakigoe = a

    def naku(self, arg=None):
        if arg:
            print(arg)
        else:
            print(self.__nakigoe)

class Cat(Animal):
    def __init__(self, a=None):
        if a:
            self._Animal__nakigoe = a
        else:
            self._Animal__nakigoe = "nya-n"
    # def naku(self, arg=None):
    #     if arg:
    #         print(arg)
    #     else:
    #         print("nya-n")


if __name__ == '__main__':
    neko = Animal("nya-n")
    neko.naku()
    neko.naku("wanwan")
    neko.naku()

    cat = Cat()
    cat.naku()

    # print("---")
    # print(cat.__nakigoe)
    # cat.__nakigoe = 'foo'
    # print(cat.__nakigoe)
    # cat.naku()

    ## __が付いてるフィールドはprivateになるのでアクセスできない
    # 
    # Traceback (most recent call last):
    # File "sample.py", line 34, in <module>
    #     print(cat.__nakigoe)
    # AttributeError: 'Cat' object has no attribute '__nakigoe'
