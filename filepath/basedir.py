import os

print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))

"""
(dev) [zaki@cloud-dev filepath]$ pwd
/home/zaki/src/python/filepath
(dev) [zaki@cloud-dev filepath]$ ls
basedir.py  sample.py
(dev) [zaki@cloud-dev filepath]$ python basedir.py 
basename:     basedir.py
dirname:      
"""

"""
(dev) [zaki@cloud-dev filepath]$ cd /
(dev) [zaki@cloud-dev /]$ python ~/src/python/filepath/basedir.py 
basename:     basedir.py
dirname:      /home/zaki/src/python/filepath
"""
