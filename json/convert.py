import json

curry = {
    'onion': 1,
    'coriander': '2tbsp',
    'cumin': '2tbsp',
    'turmeric': '2tsp',
    'white_pepper': '1tsp',
    'cooking_sake': '2tbsp',
    'salt': '1tsp',
    'sugger': '1tsp',
    'grape_seed_oil': '200g'
}

#print(json.dumps(curry))

json_string = json.dumps(curry, indent=2)
print(type(json_string))
# print(json_string)

obj = json.loads(json_string)
print(type(obj))
print(obj)

print(obj == curry)
