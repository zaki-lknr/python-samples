def error_func():
    print("error_func")
    raise Exception('curry tabetai!')
    print("unreache!")

if __name__ == '__main__':
    print("begin")

    try:
        error_func()
    except Exception as err:
        print('error ...' + str(err))
    finally:
        print('finnaly')

    print("end")
