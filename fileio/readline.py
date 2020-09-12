# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # print("hello")

    f = open("/etc/hosts")

    # # ↓ invalid syntax
    # while line = f.readline():

    line = f.readline()
    while line:
        print(line.rstrip())
        line = f.readline()

    f.close()
    