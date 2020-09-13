# -*- coding: utf-8 -*-

# Argparse チュートリアル — Python 3.8.6rc1 ドキュメント
# https://docs.python.org/ja/3/howto/argparse.html

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()

    # 上のコードで下記のようにオプション/引数指定で実行

    """
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py --help
    usage: sample.py [-h]
    
    optional arguments:
      -h, --help  show this help message and exit
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py --version
    usage: sample.py [-h]
    sample.py: error: unrecognized arguments: --version
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py --verbose
    usage: sample.py [-h]
    sample.py: error: unrecognized arguments: --verbose
    (paramiko) [zaki@cloud-dev argparse]$ python sample.py hoge
    usage: sample.py [-h]
    sample.py: error: unrecognized arguments: hoge
    (paramiko) [zaki@cloud-dev argparse]$ 
    """
