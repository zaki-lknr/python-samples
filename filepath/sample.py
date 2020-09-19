import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)

"""
(dev) [zaki@cloud-dev filepath]$ pwd
/home/zaki/src/python/filepath
(dev) [zaki@cloud-dev filepath]$ ls
sample.py
(dev) [zaki@cloud-dev filepath]$ python sample.py 
getcwd:       /home/zaki/src/python/filepath
__file__:     sample.py
(dev) [zaki@cloud-dev filepath]$ cd /
(dev) [zaki@cloud-dev /]$ python ~/src/python/filepath/sample.py 
getcwd:       /
__file__:     /home/zaki/src/python/filepath/sample.py
"""

# os.getcwd()は実行時のカレントディレクトリ
# __file__はCWDから見たソースファイルのパス
