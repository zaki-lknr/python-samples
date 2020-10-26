from abc import ABCMeta, abstractmethod

# 抽象クラス
class EsxiDevice(metaclass=ABCMeta):
    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def get(self, index):
        pass

class EsxiNetwork(EsxiDevice):
    def __init__(self):
        self.nic_list = []

    def add(self, name):
        self.nic_list.append(
            {
                'name': name
            }
        )

    def length(self):
        return len(self.nic_list)

    def get(self, index):
        return self.nic_list[index]

    # ^^^ get()やlength()を実装していないと、インスタンス生成しようとしてもエラーになる

if __name__ == '__main__':
    print("begin")

    network = EsxiNetwork()

    network.add("foo")
    network.add("bar")
    network.add("baz")

    print("len: " + str(network.length()))

