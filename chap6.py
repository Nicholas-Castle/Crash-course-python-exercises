#Dictionary
#store character information
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#working with dictionaries
alien_1  = {'color': 'red', 'armour': 10, 'points': 10}
#accessing dictionaries
print(alien_1['armour'])
new_points = alien_1['points']
print("You just earned {} points".format(new_points))
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)
#starting with and empty dictionary
alien = {}

alien['color'] = 'green'
alien['points'] = 5
print(alien)
#modifying a dictionary
alien['color'] = 'pink'
print(alien)
#tracking position
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("original x-position: {}.".format(alien_2['x_position']))
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
elif alien_2['speed'] == 'fast':
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment

print("New x-position: {}.".format(alien_2['x_position']))
del alien['points']
print(alien)

favorite_laguages = {
    'jen': 'japanese',
    'todd': 'english',
    'nick': 'spanish',
    'ruben': 'c#',
    }
#6.1
person = {
    'name': 'Addi',
    'relationship': 'Married',
    'citi': 'Kirkland',
    'Job': 'Fancy Writer',
    'traits': 'the best.',
    }
print(person)
#6.2 FAVORITE NUMBERS
fav_nums = {
    'nick': 10,
    'addi': 30,
    'nai': 25,
    'erin': 120,
    }
print(fav_nums['nick'])
print(fav_nums['addi'])
print(fav_nums['nai'])
print(fav_nums['erin'])

#glossary
glossary = {
    'list': 'A list is a data stucture where you can store numbers, strings, variables, dictionaries, and other data types in a nutable unordered list',
    'dictionary': 'is and unordered way to store key value data',
    'slice': 'you can slice an array',
    'dict': 'you can add items to a dictionary by >>> dict[key] = value',
    'n': 'is a way to add a ne line',
  }

for word, definition in glossary.items():
    print(word + "\n\tthis is a short list of words with the definitions:\n\t{}\n\n".format(definition))


#looping through dictionaries

user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

#use a for loop with key to get the keys value to get the values or both to get information for the dictionary

# key = keys of the object
# value = values of the object
# items() grabs the items in in list or dictionary
for key, value, in user.items():
    print("\nKey: " + key)
    print("Value:" + value)

# looping though
user2 = {
    'ted': 'fermi',
    'nick': 'enrico',
    'addi': 'fermi',
    }

friends = ['jhon', 'addi']
friends_to_take_the_pole = ['jhon', 'addi',  'james', 'sanders']
for name in user2.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see you favorite language is " + user2[name] + "!")

    if 'erin' not in user2.keys():
        print("\nErin ,Come take our poll")

for pollers in friends_to_take_the_pole:
    if pollers not in user2.keys():
        print("{} we invite you to take our poll".format(pollers))

#sorting keys
for name in sorted(user2.keys()):
    print(name.title() + ", Thank you for taking the poll.")

# looping through all of the values in a dictionary!!

print("the following names have been mentioned:")
for name in user2.values():
    print(name.title())

# a set is simalar to a list exept each item must be unique
for name in set(user2.values()):
    print("\n" + name.title())

#6.5 rivers# rivers = {}
rivers = {
    'nile': 'The nile is fruitful',
    'amazon': 'The amazon is the niggest river',
    'colorado': 'The colorado is long and pretty',
    }

for name, defin in rivers.items():
    print("{} and is located {}".format(defin, name))

#making aliens
aliens = []

#make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#change stats of some aliens

for random_alien in aliens[:3]:
    if random_alien['color'] == 'green':
        random_alien['color'] = 'yellow'
        random_alien['speed'] = 'medium'
        random_alien['points'] = 10
    elif random_alien['color'] == 'yellow':
        random_alien['color'] = 'red'
        random_alien['speed'] = 'medium'
        random_alien['points'] = 15

#show the first 5 aliens
for some_alien in aliens[:5]:
    print(some_alien)
print("...")

#show how many aliens have been created
print("total number of aliens: {}".format(len(aliens)))

#pizza time
pizza = {
    'crust': 'thin',
    'toppings': ['mushrooms', 'extra cheese']
    }

print("you ordered {} crust pizza with some toppings".format(pizza['crust']))

for topping in pizza['toppings']:
    print("\t{}".format(topping))

favorite_laguages = {
    'jen': ['pyhton', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskwell']
    }

for key, value in favorite_laguages.items():
    if len(value) == 1:
        print("\n" + key.title() + "'s favorite language is:")
    else:
        print("\n" + key.title() + "'s favorite languages are:")
    for m in value:
        print("\t" + m.title())

#nest dictionaries inside dictionaries

users = {
    'aeinstien': {
        'first': 'albert',
        'last': 'einstien',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: {}".format(username))
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: {}".format(full_name.title()))
    print("\tLocation: {}".format(location.title()))