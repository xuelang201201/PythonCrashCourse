# 传递任意数量的实参


# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
#
#
# make_pizza('pepperoni')
# # ('pepperoni',)
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# # ('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a %d-inch pizza with the following toppings:" % size)
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
