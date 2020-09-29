import re

string = '/path/to/sample.txt'

result = re.match(r'(?P<path>.*)/(?P<file>[^\.]*)\.(?P<ext>.*)', string)
if result:
    print("path: " + result.group(1))
    print("file: " + result.group(2))
    print("ext: " + result.group(3))
    print("---")
    print("path: " + result.group('path'))
    print("file: " + result.group('file'))
    print("ext: " + result.group('ext'))
