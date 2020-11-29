import re

string = '/path/to/sample.txt'

# s/a/A/
string = re.sub(r'a', 'A', string)
print(string)

