import inspect

def zzzz():
    print(inspect.currentframe().f_code.co_name)

if __name__ == '__main__':
    zzzz()
    # print(inspect.currentframe().f_code.co_name)
