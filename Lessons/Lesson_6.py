# Numerical Comparisons
import re


age = 18
age == 18  # True

answer = 17
if answer != 42:
    print("That is not correct")

age = 19

age < 21  # True
age <= 21  # True
age > 21  # False
age >= 21  # False

# Checking Multiple Conditions
age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >= 21:
    pass  # False

if age_0 or age_1 >= 21:
    pass  # True

age = 19
if age >= 18:
    print("You are old enough to vote")

age = 17
if age >= 18:
    print("You are old enough to vote")
else:
    print("Sorry, you are too young")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

# Practice
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points")
elif alien_color == 'yellow':
    print("You earned 10 points")
else:
    print("You earned 20 points")

# Conditional Statements & Lists
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user}, you can post a message")

# Using if statements with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    print(f"Adding {topping}")
print("Finished making your pizza")

for topping in requested_toppings:
    if topping == "green peppers":
        print(f"We are out of {topping}")
    else:
        print(f"Adding {topping}")
print("Finished making your pizza")

available_topping = ['mushrooms', 'olives',
                     'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for topping in requested_toppings:
    if topping in available_topping:
        print(f"Adding {topping}")
    else:
        print(f"We don't have {topping}")

# Practice
users = ['Heide', 'Mark', 'Bardan', 'Pat', 'Admin']
for user in users:
    if user == "Admin":
        print(f"Hello {user}, want to see a report")
    else:
        print(f"Hello {user}, welcome back")

current_users = ["Nate", "Bryce", "Rob"]
new_users = ["Ryan", "Gerry", "Bryce"]
for user in new_users:
    if user in current_users:
        print(
            f"The username {user} has already been taken. Please choose another username")
