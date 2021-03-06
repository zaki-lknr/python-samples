import os

samplepath = '/a/b/c/d/e'
print('basename: ' + os.path.basename(samplepath))
print('dirname:  ' + os.path.dirname(samplepath))

p = os.path.splitext(samplepath)
print('splitext: ' + str(p))
# splitext: ('/a/b/c/d/e', '')

samplepath = '/a/b/c/d/file.txt'
p = os.path.splitext(samplepath)
print('splitext: ' + str(p))
# splitext: ('/a/b/c/d/file', '.txt')

path, ext = os.path.splitext(samplepath)
print('path: ' + path)
print('ext:  ' + ext)

# 戻り値はタプル
path_only = os.path.splitext(samplepath)
print('path: ' + str(path_only))
print('path: ' + path_only[0])
