# -*- coding: utf-8 -*-

# Argparse チュートリアル — Python 3.8.6rc1 ドキュメント
# https://docs.python.org/ja/3/howto/argparse.html

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()

    print(args.echo)

    # 上のコードで下記のようにオプション/引数指定で実行
    # 引数(echo)が必須になり、未指定時にはエラー(簡易メッセージ)となる。
    # -hで詳しいメッセージが出力される

    """
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py 
    usage: sample.py [-h] echo
    sample.py: error: the following arguments are required: echo
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py -h
    usage: sample.py [-h] echo

    positional arguments:
    echo

    optional arguments:
    -h, --help  show this help message and exit
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge
    hoge
    """
