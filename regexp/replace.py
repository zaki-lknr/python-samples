import re

string = '/path/to/sample.txt'

# s/a/A/
string = re.sub(r'a', 'A', string)
print(string)

# 末尾の.txtを削る
string = re.sub(r'\.txt$', '', string)
print(string)

# 't'と'p'を=t=か=p=に変換
string = re.sub(r'([tp])', r'(\1)', string)
print(string)
# r'...'を使わない場合は'\\1'と書く
