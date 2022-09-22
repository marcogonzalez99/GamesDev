# Example of a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

years = ['2015', '2016', '2017', '2018', '2019']
print(years)

# Numerical Lists
numbers = list(range(1, 6))
print(numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))

# Acessing Elements in a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# Access the fourth index
print(bicycles[3])

# Access the last item of the list
print(bicycles[-1])

# Practice
names = ['Lucas', 'Kris', 'Castro', 'Madi']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

msg = "What's Up"
print(f"{msg} {names[0]}")
print(f"{msg} {names[1]}")
print(f"{msg} {names[2]}")
print(f"{msg} {names[3]}")

msg1 = "One of my best friends is"
print(f"{msg1} {names[-1]}")

# Changing Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding to a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Pop method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive.")

# Exercise 3-4
players = ['Bryce', 'Pat', 'Nate']
print(f"Hey {players[0]}, hop on lets play!")
print(f"Hey {players[1]}, hop on lets play!")
print(f"Hey {players[2]}, hop on lets play!")

# Exercise 3-5
new_player = 'Bardan'
print(f"Yo {players[0]}, bailers are failers!")
players[0] = new_player
print(f"Welcome to the team {new_player}")

# Exercise 3-6
players.append('Heide')
players.append('Mark')
players.append('Courtney')

# Exercise 3-7
weak_link = 'Pat'
players.remove(weak_link)
print(f"Sorry {weak_link}, next time buddy.")

# Sorting a list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Temp sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars = sorted(cars)
print(sorted_cars)
print(cars)

# Length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))
