#!/usr/bin/python

import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time

def run1(url):
    r = requests.get(url, verify=False)
    # print(r)
    time.sleep(random.random())
    return r
def run2(url):
    r = requests.get(url)
    # print(r)
    time.sleep(random.random())
    return r

if __name__ == "__main__":
    pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="thread")
    futures = []
    for i in range(10):
        f1= pool.submit(run1, "https://127.0.0.1:6443")
        futures.append(f1)
        f2= pool.submit(run2, "http://127.0.0.1:80")
        futures.append(f2)
        time.sleep(0.2)

    print("--------")
    print("run end!")
    print("--------")

    for future in futures:
        print(future.result())
