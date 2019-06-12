stuff = ["bag", "coat", "car"]
stuff.append("wallet")
stuff.append("cards")
stuff.append("phone")
stuff.insert(3,"insert")
del stuff[-1]
other_stuff = []
poker = stuff.pop(2)
other_stuff.append(poker)
print(other_stuff)
stuff.remove("coat")
print(stuff)