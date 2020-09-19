# import function
import sys
import os
sys.path.append((os.path.dirname(__file__) or ".") + "/..")
import function
from libs import subfunc

# from libs import subfunc

if __name__ == '__main__':
    function.curry()
    subfunc.spice()
