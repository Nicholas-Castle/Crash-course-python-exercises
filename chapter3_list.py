# add, remove, del to list
people = ["Pual Rand", "Sabastion", "Lincon"]
print(people[2] + " Cant make it")
del people[-1]
people.append("Mario Batali")

def invites():
    for i in people:
        print(i + " are invited to the best party evar!")
invites()
print("More people are coming to the dinner and we found a bigger table!")
people.append("C3PO")
people.append("Kenshi")
people.append("Tomas the Mutha Fuckin train")
invites()
print( people.pop() + " Im sorry people and robits the table will only fit two")
print( people.pop() + " Im sorry people and robits the table will only fit two")
print( people.pop() + " Im sorry people and robits the table will only fit two")
print( people.pop() + " Im sorry people and robits the table will only fit two")
print(people)
invites()
del people[0]
del people[0]
print(people)

#organizing a list
cars = ["BMW", "Lexus", "Ford", "Chevy"]
cars.sort()
print(cars)
#sort permanent 
#sort reverse permanent
cars.sort(reverse = True)
print(cars)
#temporay sort 
print("Original List")
print(cars)
print("\nSorted list")
print(sorted(cars))
print("original list again")
print(cars)
#USE sorted instead or sort!
#Printing a list in reverse order
cars.reverse()
print(cars) 
#Reverse is permanent however you can reverse back to the original list
#Finding the lenght of a list
how_many_cars = len(cars) 
print(how_many_cars)

#3.8
locations = ["Italy", "Maine", "New Zeland", "Costa Rica", "Egypt"]
print(locations)
locations.sort(reverse = True)
print(locations)
print(locations)
print(sorted(locations))
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse = True)
print(locations)
#Advoiding index errors

games = ["COD", "Destiny", "Overwatch"]
#sliceing a list with a loop
print("My top two games are:")
for game in games[-2:]:
    print(game)
#copying a list
my_foods = ['pizza', 'mac n cheese', 'falafel']
friends_foods = my_foods[:]
friends_foods.append('sammichs')
my_foods.append('honey')
print('My favorite foods are')
print(my_foods)
print('\nMy friends favorite foods are ')
print(friends_foods)
#4.10
cards = ['magic', 'dragon ball z', 'yugiho', 'spades',' harry potter', 'catan']
print('The first three items in the list are:')
print(cards[:3])
print('\nThe the items in the middle are')
print(cards[-1:])
print('\nThe last three items in the list are:')
print(cards[-3:])
#4.11
my_treats = ['apples', 'oranges', 'peanuts', 'jerky']
friends_treats = my_treats[:]
my_treats.append('ice cream')
friends_treats.append('hot dogs')
my_treats.append('pop tarts')
friends_treats.append('chia pudding')
print('My favorite treats are:')
print(my_treats)
print('\nMy friends favorite treats are: ')
print(friends_treats)
#more loops
for mytreat in my_treats:
    print(mytreat)
for friends_treat in friends_treats:
    print('\n' + friends_treat)
#tuples

#looping through tuples
dimensions = (200, 50)
#writing over a tuple
print('originals ds')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
#4.13
basic_meals = ('fried chicken', 'steak', 'mashed potatoes', 'bread', 'salad')
for meal in basic_meals:
    print(meal)
basic_meals = ('fried chicken', 'steak', 'mashed potatoes', 'tacos', 'pie')
for food in basic_meals:
    print(food)