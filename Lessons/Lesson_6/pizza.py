def make_pizza(size, *toppings):
    print(f"Maing a {size},-inch pizza with the following toppings")

    for topping in toppings:
        print("- " + topping)