magicians = ['gandolf', 'merlin', 'alice']
for magician in magicians:
    print(magician.title() + ", is amazing!")
    print(magician.title() + " that was an amazing trick!\n" )
print("Thank you everyone for the fantastic magic show!")

#4.1
pizzas = ['Cheese','Peperoni','Pinapple','Ham','Veggie']
for pizza in pizzas:
    print("The best kinds of pizza are " + pizza)
print('pizza is the best')

#4.2 animals
animals = ['cat','dog','moose','hamster','gerbil']
for animal in animals:
    print("A" + animal.title() + " would be my next pet\n")
print('These animals all have four legs')
# numerical lists
# range()
for value in range(1, 5):
    print(value)

for i in range(1, 6):
    print(i)
#using range to make a list of numbers
# lsit is a way to create a list and range basiclly generates numbers -1
numbers = list(range(1, 11))
print(numbers)
#range can also skip numbers by passing in another argument
even_numbers = list(range(2,21,2))
print(even_numbers)
#putting squares in a list
squares = []
for j in range(1, 11):
    squares.append(j**2)
    digits = [j**2 for j in range(1,21)]
print(digits)
print(squares)
#simple statistics with a list of numbers
for j in range(1, 11):
    squares.append(j**2)
    digits = [j**2 for j in range(1,21)]
print(digits)
#4.3
# counting
for count in range(1,21):
    print(count)
#millon dollar list
million = [c for c in range(1, 1000001)]
#print(million)
#min max million
print(max(million))
print(min(million))

#sum everthin up to a million
print(sum(million))
#list of odd numbers 1 - 20
odd = []
for g in range(1,21, 2):
    odd.append(g)
print(odd)
#multiples of three
multi3 = []
for h in range(3, 31):
    multi3.append(h * 3)
print(multi3)
#4.8 cubes
cubes = []
for q in range(1,11):
    cubes.append(q**3)
print(cubes)
#list comprehension cubes
list_cube = [d**3 for d in range(1, 11)]
print(list_cube)
# working with part of a list
