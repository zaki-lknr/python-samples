# -*- coding: utf-8 -*-

# Argparse チュートリアル — Python 3.8.6rc1 ドキュメント
# https://docs.python.org/ja/3/howto/argparse.html

import argparse

if __name__ == '__main__':
    data = 'aaa'

    parser = argparse.ArgumentParser()
    ### これは-vのあとに引数が必要
    ### -v foobar など
    ### -v ごとなければNone
    parser.add_argument("-o", "--opt", help="option")

    ### store_true:
    ## -v があればTrue / なければFalse
    ## -v の後に引数があるとエラー
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")


    args = parser.parse_args()
    d = args.opt or data
    print(d)

    print(args.verbose)
