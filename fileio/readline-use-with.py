# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # print("hello")

    with open("/etc/hosts") as f:
        for line in iter(f.readline, ''):
            print(line.rstrip())

