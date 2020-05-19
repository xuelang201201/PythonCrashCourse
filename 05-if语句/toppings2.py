"""使用 if 语句处理列表"""

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    # 检查特殊元素
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print("Adding %s." % requested_topping)

print("\nFinished making your pizza!")

#  确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding %s." % requested_topping)
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding %s." % requested_topping)
    else:
        print("Sorry, we don't have %s." % requested_topping)

print("\nFinished making your pizza!")
