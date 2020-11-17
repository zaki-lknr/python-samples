import myiter

my = myiter.MyIterSample()
my.add(10)
my.add(20)
my.add(30)
for z in my:
    print(z)
print("---")

for i,z in enumerate(my):
    print(i, " : ", z)

print("---")

mylist = ['foo', 'bar', 'baz']

for item in mylist:
    print(item)

print("---")
for index, item in enumerate(mylist):
    print(index, " : ", item)
print("---")


# for item in iter(mylist):
#     print(item)

item = iter(mylist)
print(next(item))
print(next(item))
print(next(item))
print(next(item))  # StopIteration

print("end") # unreachable 
