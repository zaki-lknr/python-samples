# -*- coding: utf-8 -*-

# Argparse チュートリアル — Python 3.8.6rc1 ドキュメント
# https://docs.python.org/ja/3/howto/argparse.html

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    args = parser.parse_args()

    if args.verbosity:
        print("verbosity turned on")


    # 上のコードで下記のようにオプション/引数指定で実行。
    # オプション引数(--verbosity)を指定できる。
    # ただしオプションの引数(実行例では`1`や`2`)が無い場合はエラー。
    # -hで詳しいメッセージが出力される。

    """
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --verbosity 1
    verbosity turned on
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --verbosity 2
    verbosity turned on
    (paramiko) [zaki@cloud-dev argparse]$ 
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py 
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --help
    usage: sample-optional-arguments.py [-h] [--verbosity VERBOSITY]

    optional arguments:
    -h, --help            show this help message and exit
    --verbosity VERBOSITY
                            increase output verbosity
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --verbosity
    usage: sample-optional-arguments.py [-h] [--verbosity VERBOSITY]
    sample-optional-arguments.py: error: argument --verbosity: expected one argument
    (paramiko) [zaki@cloud-dev argparse]$ 
    """
