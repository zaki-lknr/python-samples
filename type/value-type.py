string_value = 'hogehoge'
int_value = 123

int_list = [1, 2, 3, 'str']
dict_sample = {'foo':1, 'bar':2}

if type(string_value) == str:
    print("string_value is str")

if type(int_value) == int:
    print("int_value is int")

if type(int_list) == list:
    print("int_list is list")
if type(int_list[0]) == int:
    print("int_list[0] is int")
if type(int_list[3]) == str:
    print("int_list[3] is str")

if type(dict_sample) == dict:
    print("dict_sample is dict")
