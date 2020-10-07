def func():
    result = 0
    return result == 1
    
single = 'hoge"hoge'
print(single)

double = "hoge'hoge"
print(double)

result = True
if not result:
    print("true")

val = 1
if val != 0:
    print("not zero")

r = func()
print("result: " + str(r))


print("hello, {}".format("ansible"))
print('hello, {}'.format("ansible"))
