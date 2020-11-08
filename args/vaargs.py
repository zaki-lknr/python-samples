# 可変長引数

def sample_func(arg1, *args):
    print('sample_func begin')
    print('arg1: ' + arg1)
    print('type of args:' + str(type(args)))
    print('args len: ' + str(len(args)))
    print(args)
    print('sample_func end')

if __name__ == '__main__':
    print('main begin')
    sample_func('hoge')
    print('---')
    sample_func('hoge', 'foo')
    print('---')
    sample_func('hoge', 'foo', 'bar')
    print('---')
    sample_func('hoge', 'foo', 'bar', 'baz')
