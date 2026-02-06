from concurrent.futures import ThreadPoolExecutor
import time

def sample_function(argf):
    print("sample_function begin (arg:" + argf + ")")
    time.sleep(3)
    print("sample_function end")

    return argf

if __name__ == '__main__':
    # sample_function("hello")

    pool = ThreadPoolExecutor(max_workers=2)

    f1 = pool.submit(sample_function, "hello1")
    f2 = pool.submit(sample_function, "hello2")

    print("started")

    r = f2.result()
    print(r)
    r = f1.result()
    print(r)
