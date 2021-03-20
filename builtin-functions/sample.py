# https://docs.python.org/ja/3/library/functions.html#getattr

class GetAttrSample:
    def my_function(args="no args"):
        print("this is my_function() args: " + args)

if __name__ == '__main__':
    print("begin")
    gas = GetAttrSample
    gas.my_function()
    gas.my_function("aaa")

    zzz = getattr(gas, 'my_function')
    zzz()
    zzz('hoge')
