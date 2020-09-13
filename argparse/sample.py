# -*- coding: utf-8 -*-

# Argparse チュートリアル — Python 3.8.6rc1 ドキュメント
# https://docs.python.org/ja/3/howto/argparse.html

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("square", help="display a square of a given number", type=int)
    args = parser.parse_args()

    print(args.echo)
    print(args.square**2)

    # 上のコードで下記のようにオプション/引数指定で実行
    # 引数(echo)が必須になり、未指定時にはエラー(簡易メッセージ)となる。
    # -hで詳しいメッセージが出力される。
    # その際は`add_argument()`の引数にhelp=(string)でセットしたものが表示される。
    # 更にtype=intを指定すると、integerとして扱われる。

    """
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py 
    usage: sample.py [-h] echo square
    sample.py: error: the following arguments are required: echo, square
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py -h
    usage: sample.py [-h] echo square

    positional arguments:
    echo        echo the string you use here
    square      display a square of a given number

    optional arguments:
    -h, --help  show this help message and exit
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge 4
    hoge
    16
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge four
    usage: sample.py [-h] echo square
    sample.py: error: argument square: invalid int value: 'four'
    """
