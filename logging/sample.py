import logging

if __name__ == '__main__':
    print("hello world")

    # デフォルトはwarning以上
    # この設定を入れるとdebug以上が出力される
    logging.basicConfig(level=logging.DEBUG, filename="./app.log")

    logging.critical('これはcritical')
    logging.error('これはerror')
    logging.warning('これはwarning')
    logging.info('これはinfo')
    logging.debug('これはdebug')
