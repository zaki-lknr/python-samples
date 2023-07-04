def get_lists():
    list1 = [1,2,3]
    list2 = ['foo', 'bar', 'baz']
    return list1, list2

if __name__ == '__main__':
    a, b = get_lists()
    a.append(4) # OK
    print(a)    # [1,2,3,4]
    print(b)    # ['foo', 'bar', 'baz']

    t = get_lists()
    t.apppend([9, 8, 7])  # tupleなのでNG
