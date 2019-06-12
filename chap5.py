#using conditionals in a loop
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# checking to see if ian item is in a list
toppings = ['pep','mushrooms','ham']
print('ham' in toppings)
print('toms' in toppings)
#simple if statements
# if 10 < 20:
#    print('less than')
age = 2
if age < 4:
    print('Free')
    price = 0
elif age < 18:
    print('5 dollars')
    price = 5
else:
    print('20 dollars')
    price = 20
print('Your addmisions is going to cost you {} dollars'.format(price))
#toppings
toppings = ['peperoni', 'ham', 'coppa']

if 'tomatoes' not in toppings:
    print('add mushrooms please')
if 'coppa' in toppings:
    print('adding coppa')
if 'ham' in toppings:
    print('adding hame')

#5.3 Alien colors one
points = 10
multiplier = 2
alien_color = 'red'
if alien_color == 'green':
  points = points + 5
  score = 5
  print('You just earned {} points'.format(score))
elif alien_color == 'yellow':
    points = points + 10
    score = 10
    print('You just earned {} points'.format(score))
else:
    print('2X multiplier!')
    points = points + 15
    score =  multiplier + points
    for point in range(points):
        print((point + 1) * multiplier + points)
    print('You just earned {} points'.format(score))

#stages of life with user input
#stages_of_life = int(input("Please enter your age"))
#if stages_of_life < 2:
#    print('Baby')
#elif stages_of_life < 4:
#    print('toddler')
#elif stages_of_life < 13:
#    print('kid')
#elif stages_of_life < 20:
#    print('teenager')
#elif stages_of_life < 65:
#    print('adult')
#else:
#    print('elder')
#favorite fruit
#fruits = ['apples', 'oranges', 'pears']
#users_fruit = input('Please enter a fruit.')
#if users_fruit in fruits:
#    print("{} is my favorite fruit too!".format(users_fruit))
#if users_fruit not in fruits:
#    fruits.append(users_fruit)
#    print(fruits)
#    print("{} I'm going to add this to my fruit list".format(users_fruit))

#checking special items in a list
#phones = []
#for phone in phones:
#    if phone == 'ipad':
#        print("Sorry where all sold out!")
#else:
#     print("we have plenty please look")
#check if a list is not empty
#  if phones == []:
#       print('would you like to buy a phone?')
#multiple lists
#avail_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'extra cheese']

#requested_toppings = ['mushrooms', 'olives', 'green peppers']

#for requested_topping in requested_toppings:
#    if requested_topping in avail_toppings:
#        print("adding " + requested_topping + ".")
#    else:
#       print("sorry we dont have " + requested_topping + ".")

#print('\nfinished making your pizza')
#5.8 Hello admin
username = ['james','tony']
if username == []:
    print("Lets get some users!")
for user in username:
    if user == 'admin':
        print('Welcome back administrator')
    else:
        print("hello " + user)

#5.10 checking username
current_users = ['james','tony','mark','tim','jane']
new_users = ['nick', 'addi', 'mazzy', 'louie', 'Tony', 'jane']
for user in new_users:
    if user in current_users:
        print(user + " is not available please enter a new user name")
    else:
        print(user + " that name is available!")


#5.11 ordinal numbers
numbers = [1, 2, 3, 4 , 5 , 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    if number == 2:
        print(str(number) + "nd")
    if number == 3:
        print(str(number) + "rd")
    if number > 3:
        print(str(number) + "th")