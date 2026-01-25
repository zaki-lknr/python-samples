import fcntl
import os
import time

file_path_ap = './flock.txt'

with open(file_path_ap, 'a+') as f:
    try:
        fcntl.flock(f, fcntl.LOCK_EX)
        print("file locked")
        f.seek(0)
        data = f.read()
        print(data)

        print("sleeping...")
        time.sleep(5)
        print("sleeped")

        f.truncate(0)
        output = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        f.write(output)

        f.flush()
        os.fsync(f.fileno())
        print("file write done")
    finally:
        fcntl.flock(f, fcntl.LOCK_UN)
        print("file unlocked")
