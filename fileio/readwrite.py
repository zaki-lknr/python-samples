file_path = './sample.txt'

with open(file_path, 'w+') as f:
    # w+ はread/write可能
    # ただしopen()の時点で既存ファイルは空
    data = f.read()

    print(data)

    f.write("aaa")

    f.seek(0)
    data = f.read()

    print(data)
