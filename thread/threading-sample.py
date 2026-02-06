import threading
import time

def sample_function(argf):
    print("sample_function begin (arg:" + argf + ")")
    time.sleep(3)
    print("sample_function end")


if __name__ == '__main__':
    # sample_function("hello")

    th1 = threading.Thread(target=sample_function, args=("hello1",))
    th2 = threading.Thread(target=sample_function, args=("hello2",))
    th1.start()
    th2.start()

    print("started")

    th1.join()
    th2.join()

    print("function all end")
