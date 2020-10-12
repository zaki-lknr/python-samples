#!/usr/bin/env python

print("begin")

dict1 = {"key1": "value1", "key2": "value2"}
print(dict1)

dict2 = dict(key1="value1", key2="value2")
print(dict2)

if dict1 == dict2:
    # 辞書の一致判定の処理系は未チェックだけど、このコードだとtrueになる
    print("equal")
else:
    print("not equal")

print("end")
