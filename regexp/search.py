import re

string = '/path/to/sample.txt'

# matchしない
m = re.match(r'sample', string)
if m:
    print("match(/sample/) is match")

# .*で先頭部分の文字列も含んでるのでmatchする
m = re.match(r'.*sample', string)
if m:
    print("match(/.*sample/) is match")

# searchなら/sample/でマッチする
m = re.search(r'sample', string)
if m:
    print("search(/sample/) is match")

