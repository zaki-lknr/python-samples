def error_func():
    print("error_func")
    raise Exception('exception!')
    print("unreache!")

if __name__ == '__main__':
    print("begin")
    error_func()

    print("end")
