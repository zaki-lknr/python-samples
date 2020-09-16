class Animal:
    def set_nakigoe(self, a):
        self.nakigoe = a

    def naku(self):
        print(self.nakigoe)

neko = Animal()
neko.set_nakigoe("nya-n")
neko.naku()
