# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # print("hello")

    f = open("/etc/hosts")

    for line in iter(f.readline, ''):
        print(line.rstrip())

    f.close()
