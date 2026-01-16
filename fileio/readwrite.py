file_path_wp = './sample1.txt'
file_path_ap = './sample2.txt'

with open(file_path_wp, 'w+') as f:
    # w+ はread/write可能
    # ただしopen()の時点で既存ファイルは空
    data = f.read()

    print(data)

    f.write("aaa")

    f.seek(0)
    data = f.read()

    print(data)

with open(file_path_ap, 'a+') as f:
    f.seek(0)
    data = f.read()
    print(data)

    f.truncate(0)
    f.write("bbb")
