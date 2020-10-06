def function(arg1, arg2):
    print("arg1: " + arg1)
    print("arg2: " + arg2)

if __name__ == '__main__':
    print("begin")
    function("a1", "a2")
    print("---")
    function(arg1="val1", arg2="val2")
    print("---")
    function(arg2="bar", arg1="foo")
