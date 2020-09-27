# -*- coding: utf-8 -*-

# Argparse チュートリアル — Python 3.8.6rc1 ドキュメント
# https://docs.python.org/ja/3/howto/argparse.html

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("square", help="display a square of a given number", type=int)
    #parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", type=int)
    args = parser.parse_args()

    # print(args.echo)
    # print(args.square**2)
    answer = args.square**2
    if args.verbose == 2:
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbose == 1:
        print("{}^2 == {}".format(args.square, answer))
    else:
        print(answer)

    # 上のコードで下記のようにオプション/引数指定で実行
    # 引数(echo, square)は必須・未指定時にはエラー(簡易メッセージ)となる。
    # -hで詳しいメッセージが出力される。
    # その際は`add_argument()`の引数にhelp=(string)でセットしたものが表示される。
    # 更にtype=intを指定すると、integerとして扱われる。
    #
    # -v|--verboseはオプションなので無くても良いし順序も問われない。
    # ただしtype=intなので-v指定時は引数に数値が必要

    """
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py 
    usage: sample.py [-h] [-v] echo square
    sample.py: error: the following arguments are required: echo, square
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py -h
    usage: sample.py [-h] [-v] echo square

    positional arguments:
    echo           echo the string you use here
    square         display a square of a given number

    optional arguments:
    -h, --help     show this help message and exit
    -v, --verbose  increase output verbosity
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge 4
    16
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge 4 -v
    usage: sample.py [-h] [-v VERBOSE] echo square
    sample.py: error: argument -v/--verbose: expected one argument
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge 4 -v 1
    4^2 == 16
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge 4 -v 2
    the square of 4 equals 16
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge 4
    16
    """
