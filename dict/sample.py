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

# add item to dict
print("--- add item to dict ---")
dict1['key3'] = "value3"

if dict1 == dict2:
    print("equal")
else:
    # ここでは不一致
    print("> not equal")

dict2['key3'] = "value3"
if dict1 == dict2:
    # ここでは一致
    print("> equal")
else:
    print("not equal")

# 上書き
dict1['key1'] = "hoge"
if dict1 == dict2:
    print("equal")
else:
    # ここでは一致
    print("> not equal")
    print(dict1['key1'])

print("end")
