#!/usr/bin/env python

print("begin")

dict1 = {"key1": "value1", "key2": "value2"}
print(dict1)


if dict1['key1'] == 'value1':
    print("key1 == value1")

# if dict1['hoge'] == None:
#     print("hoge is None")

# ^^^ KeyError: 'hoge' 例外になる

if 'key1' in dict1:
    print('dict1 has key1')

if not 'hoge' in dict1:
    print('dict1 not has hoge')

if not dict1.get('hoge'):
    print('dict1 has not hoge (part2)')
