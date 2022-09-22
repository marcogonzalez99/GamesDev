# Looping through a entier list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, great trick!")

print("\n")

for magician in magicians:
    print(f"{magician.title()}, great trick!")
    print("Can we see another one?")

print("Thank you for the show!")

# Example
animals = ['dog', 'cat', 'elephant']
for animal in animals:
    print(f"A {animal} would make a great pet")
print("I want all of them")

# Slicing a list
players = ['bardan', 'pat', 'heide', 'mark']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3])

# Looping through a slice
players = ['bardan', 'pat', 'heide', 'mark']
print("The first three players on my team")
for player in players[:3]:
    print(player.title())

# Practice
games = ['Super Mario', 'Zelda', 'Donkey Kong', 'Sonic',
         'Duck Hunter', 'Mortal Kombat', 'Street Fighter']
print(f"The first three games are {games[:3]}")
print(f"The middle games are {games[3:5]}")
print(f"The last three games are {games[-3:]}")

# List Comprehensions
numbers = [num for num in range(1, 11)]
print(numbers)

# Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# Practice
even_numbers = [val*2 for val in range(1, 11)]
print(even_numbers)

menu = ('sushi', 'katsu', 'ramen', 'pasta', 'burger')
for item in menu:
    print(item)
