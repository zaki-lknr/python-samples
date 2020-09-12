# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    # print("hello")

    pattern = '(\d+)\s+(.+)\s+\[(.+)\] (.+\.vmx)\s+(\S+)\s+(\S+)'

    f = open("vmsvc-getallvms.txt")
    for line in iter(f.readline, ''):
        # print(line.rstrip())
        result = re.match(pattern, line)

        if result:
            print("vid: " + result.group(1))
            print("vm: " + result.group(2))
            print("ds: " + result.group(3))
            print("file: " + result.group(4))
            print("guest: " + result.group(5))
            print("version: " + result.group(6))


    f.close()
