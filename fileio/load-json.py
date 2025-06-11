import json

with open('./sample.json') as f:
    # print(f.read())
    obj = json.load(f)
    print(obj)
