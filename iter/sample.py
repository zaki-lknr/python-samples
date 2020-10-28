import myiter

my = myiter.MyIterSample()
my.add(10)
my.add(20)
my.add(30)
for z in my:
    print(z)

print("---")

mylist = ['foo', 'bar', 'baz']

for item in mylist:
    print(item)

# for item in iter(mylist):
#     print(item)

item = iter(mylist)
print(next(item))
print(next(item))
print(next(item))
print(next(item))  # StopIteration

print("end") # unreachable 
