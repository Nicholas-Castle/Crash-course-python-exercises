#message = input("tell me something and I'll repeat it back to you: ")
#print(message)

#writing clear prompts
#name = input("Please enter your name: ")
#print("Hello {}!".format(name))

#prompt = "If youn tell us who you are, we can personalize the message you see"
#prompt += "\nWhat is your first name?: "

#name = input(prompt)
#print("\nHello, {}!".format(name))

#using an uint in input
#age = input("How old are you?: ")
#age = int(age)
#print(age >= 18)

#rollercoaster
#height = input("How tall are you, in inches?: ")
#height = int(height)

#if height >= 36:
#    print("Your tall enough to ride the roller coaster")
#else:
#    print("Almost sorry you be able to ride the roller coaster when your older")

#the modulo operatorrrrr
#print(4 % 3)
#print(5 % 3)
#print(6 % 3)

#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)

#if number % 2 == 0:
#    print("\nThe number {} in even".format(str(number)))
#else:
#    print("\nThe number {} is odd".format(str(number)))

#7.1 rental car
#rental_car = input("What kind of car would you like to drive?: ")
#print("Hmmm let me check if we have a {} in the lot.".format(rental_car))

#7.2 Resturaunt
#dinner_group = input("How many people will be in your group tonight?: ")
#dinner_group = int(dinner_group)

#if dinner_group > 8:
#    print("You'll have to wait 30 minutes until you can be seated")
#else:
#    print("Come your table is ready")

#7.3 Multiples of ten
#number = input("Give me a number and I'll tell you whether it's a multiple of ten or not: ")
#number = int(number)

#if number % 10 == 0:
#    print("you number is a multiple of ten congratz")
#else:
#    print("try agian")

#while loop time
#current_num = 1
#while current_num <= 5:
#    print(current_num)
#    current_num += 1

#letting the game play until the person says to stop
#prompt = "\nTell me something, and I'll reapet it back to you: "
#prompt += "\nEnter 'quit' to end the program"
#message = ""
#while message != 'quit':
#    message = input(prompt)

#    if message != 'quit:'
#        print(message)
#flags
#active = True
#while active:
#    message = input(prompt)
#
#    if message == 'quit':
#        active = False
#    else:
#        print(message)

#using break to stop a while loop

#prompt = "\nPlease enter the name of a city you've visited:"
#prompt += "\n(Enter 'QUIT' when you're finished)"

#while True:
#    city = input(prompt)

#    if city == 'QUIT':
#        break
#    else:
#        print("I'd love to go to {}!".format(city.title()))

#using continue in a while loop
#current_number = 0
#while current_number < 10:
#    current_number += 1
#    if current_number % 2 == 0:
#        continue
#
#   print(current_number)

#advioding infinite loops

#prompt = "\nPlease enter your toppings: "
#prompt += "\nTo exit tpye 'QUIT'"
#toppings = []

#while True:
#    message = input(prompt)
#
#    if message == 'QUIT':
#        print("Thank you for your order!\nYou ordered a large pizza with: ")
#        for topping in toppings:
#            print("{}".format(topping))
#        break
#    else:
#        print(message)
#        toppings.append(message)

#7.5 Movie tickets
#adult = 20
#child = 13
#toddler = 0
#active = True

#prompt = input("please enter your age: ")

#while active:
#    prompt = int(prompt)
#    if prompt < 3:
#        toddler = "free"
#        print("your cost of admissions is {} for toddlers and younger".format(str(toddler)))
#        active = False
#    elif prompt <= 12:
#        print("your cost of admissions is {} dollars for an child's ticket".format(str(child)))
#        active = False
#    else:
#        print("your cost of admissions is {} dollars for an adult ticket".format(str(adult)))
#        active = False


