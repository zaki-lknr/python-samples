#!/usr/bin/python

import requests
import threading
import time

def run1():
    r = requests.get("https://127.0.0.1:6443", verify=False)
    print(r)
def run2():
    r = requests.get("http://127.0.0.1:80")
    print(r)

if __name__ == "__main__":
    for i in range(10):
        th1= threading.Thread(target=run1)
        th1.start()
        th2= threading.Thread(target=run2)
        th2.start()
        time.sleep(0.2)
