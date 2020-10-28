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
