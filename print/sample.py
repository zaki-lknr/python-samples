# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("hello")

    f = open("/etc/hosts")

    data = f.read()
    f.close()

    # print(data)
    print(data, end="")
