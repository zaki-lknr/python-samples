# -*- coding: utf-8 -*-

# Argparse チュートリアル — Python 3.8.6rc1 ドキュメント
# https://docs.python.org/ja/3/howto/argparse.html

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    if args.verbosity:
        print("verbosity turned on")
    if args.verbose:
        print("verbose turned on")


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
    usage: sample-optional-arguments.py [-h] [--verbosity VERBOSITY] [-v]

    optional arguments:
    -h, --help            show this help message and exit
    --verbosity VERBOSITY
                            increase output verbosity
    -v, --verbose         increase output verbosity
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --verbosity
    usage: sample-optional-arguments.py [-h] [--verbosity VERBOSITY]
    sample-optional-arguments.py: error: argument --verbosity: expected one argument
    (paramiko) [zaki@cloud-dev argparse]$ 
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --verbose
    verbose turned on
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --verbose 1
    usage: sample-optional-arguments.py [-h] [--verbosity VERBOSITY] [--verbose]
    sample-optional-arguments.py: error: unrecognized arguments: 1
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py --verbose true
    usage: sample-optional-arguments.py [-h] [--verbosity VERBOSITY] [--verbose]
    sample-optional-arguments.py: error: unrecognized arguments: true
    (paramiko) [zaki@cloud-dev argparse]$ python sample-optional-arguments.py -v
    verbose turned on
    """
