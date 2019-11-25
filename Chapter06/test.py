people = [
    {
        'first': 'susan',
        'last': 'zeng',
        'location': 'guangzhou',
    },
    {
        'first': 'hedy',
        'last': 'he',
        'location': 'guangzhou'
    },
    {
        'first': 'joanna',
        'last': 'zhang',
        'location': 'haikou'
    }
]

for person in people:
    print(person)


pets = [
    {
        'animal': 'cat',
        'owner': 'wang'
    },
    {
        'animal': 'dog',
        'owner': 'zhang'   
    }
]

for pet in pets:
    print(pet)


favorite_places = {
    'susan': ['guangzhou','shanghai'],
    'joanna': ['haikou','sanya'],
    'hedy': ['hangzhou','guangzhou']
}

for name,places in favorite_places.items():
    print(name,places)


favorite_nums = {
    'susan': [34,45],
    'joanna': [34,76],
    'hedy': [876,32]
}

for name,nums in favorite_nums.items():
    print(name,nums)

cities = {
    'shanghai': {
        'country': 'China',
        'population': '5M',
        'fact': 'jah'
    },
    'paris': {
        'country': 'French',
        'population': '1M',
        'fact': 'sdf'
    }
}

for city,info in cities.items():
    print(city,info)