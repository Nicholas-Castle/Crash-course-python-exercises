#6.7
people = [{
    'person1': {
        'first': 'Nick',
        'last': 'castle',
        'location': 'home',
        'age': 31,
        },
    'person2': {
        'first': 'louie',
        'last': 'thaha',
        'location': 'home',
        'age': 7,
        },
    'person3': {
        'first': 'Addi',
        'last': 'Haberly',
        'location': 'brix',
        'age': 23,
        },
    }
]
for person in people:
    for k, v in person.items():
        print("\n")
        print(k)
        for k, l in v.items():
            print(k, l)


#pet dictionaries
pets = [{
    'cat': {
        'breed': 'tabby',
        'legs': 4,
        'friendly': 'no',
        'whines': 'yes',
    },
    'dog': {
        'breed': 'german shepard',
        'legs': 4,
        'friendly': 'most of the time',
        'whines': 'yes',
    },
    'hamster': {
        'breed': 'gerbil',
        'legs': 4,
        'friendly': 'yes',
        'whines': 'no',
    },
    'frog': {
        'breed': 'toad',
        'legs': 2,
        'friendly': 'yes',
        'whines': 'no',
    },
    'lion': {
        'breed': 'big cat',
        'legs': 4,
        'friendly': 'no',
        'whines': 'no',
    },
}
]
for pet in pets:
    for type, details in pet.items():
        print("\n")
        print(type)
        for info, traits in details.items():
            print("\t" + info + ": " + str(traits))


#favorite places 6.9

favorite_places = {
    'addi': 'malta',
    'nick': 'italy',
    'mazzy': 'comfy bed',
    }
print("\n")
for name, place in favorite_places.items():
    if name == 'mazzy':
        print("\t{}'s favorite place is a {}".format(name, place))
    else:
        print("\t{}'s favorite place is {}".format(name, place))

#favorite numbers 6.10

favorite_numbers =  {
    'nick': ['13', '80'],
    'addi': '2',
    'mazzy': '7',
    'louie': ['77', '12'],
    'greg': ['10']
    }
for name, numbers in favorite_numbers.items():
    print(name + "'s favorite number is:")
    for number in numbers:
        print(number)

#cities

cities = {
    'seattle': {
        'population': '3.5 million',
        'country': 'USA',
        'fact': 'The land that is now the city of Seattle has been inhabited for at least 4,000 years.',
    },
    'denver': {
        'population': '2.9 million',
        'country': 'USA',
        'fact': 'At an elevation of 5,280 feet, Denver is nicknamed the "Mile High City" because it sits exactly one mile above sea level.',
    },
    'anchorage': {
        'population': '294,000',
        'country': 'USA',
        'fact': 'There are 105 miles of groomed cross-country ski trails in Anchorage.',
    },
}

for city, stats in cities.items():
    print("\nCity: " + city)
    full_info = stats['population']
    country = "Country " + stats['country']
    facts = stats['fact']

    print("\t" + country)
    print("\t" + full_info.title())
    print("\t" + facts.title())

