import os

print(os.path.dirname(".") or ".")
print(os.path.dirname(__file__) or ".")

path = os.path.dirname(__file__)
hoge = None

print('"' + path + '"')
print(hoge)