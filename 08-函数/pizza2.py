def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a %d-inch pizza with the following toppings:" % size)
    for topping in toppings:
        print("- " + topping)
