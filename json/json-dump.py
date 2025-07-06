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

with open('data.json', mode='w') as f:
    json.dump(curry, f, indent=2)
