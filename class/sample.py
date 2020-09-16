class Animal:
    def __init__(self, a):
        self.nakigoe = a

    def naku(self, arg=None):
        if arg:
            print(arg)
        else:
            print(self.nakigoe)

neko = Animal("nya-n")
neko.naku()
neko.naku("wanwan")
neko.naku()
