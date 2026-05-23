import json

curry = {
    'onion': 1,
    'coriander': '大2',
    'cumin': '大2',
    'turmeric': '小2',
    'white_pepper': '小1',
    'cooking_sake': '大2',
    'salt': '小1',
    'sugger': '小1',
    'grape_seed_oil': '200グラム'
}

json_string = json.dumps(curry, indent=2)
print(json_string)

json_string = json.dumps(curry, indent=2, ensure_ascii=False)
print(json_string)
