class Animal:
    def __init__(self, a):
        self.nakigoe = a

    def naku(self, arg=None):
        if arg:
            print(arg)
        else:
            print(self.nakigoe)

class Cat(Animal):
    def __init__(self, a=None):
        if a:
            self.nakigoe = a
        else:
            self.nakigoe = "nya-n"
    # def naku(self, arg=None):
    #     if arg:
    #         print(arg)
    #     else:
    #         print("nya-n")

neko = Animal("nya-n")
neko.naku()
neko.naku("wanwan")
neko.naku()

cat = Cat()
cat.naku()
