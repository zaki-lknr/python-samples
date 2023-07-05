def get_tuple():
    list1 = [1,2,3]
    list2 = ['foo', 'bar', 'baz']
    return list1, list2   # , を使うとtupleとして定義される

if __name__ == '__main__':
    a, b = get_tuple()
    print(a)    # [1,2,3,4]
    print(b)    # ['foo', 'bar', 'baz']

    t = get_tuple()
    t.apppend([9, 8, 7])  # tupleなのでNG
