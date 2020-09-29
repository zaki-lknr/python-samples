import re

string = '/path/to/sample.txt'

result = re.match(r'(.*)/([^\.]*)\.(.*)', string)
if result:
    print("path: " + result.group(1))
    print("file: " + result.group(2))
    print("ext: " + result.group(3))
