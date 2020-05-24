"""
三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），
并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
"""


def make_sandwich(*items):
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding %s to your sandwich." % item)
    print("Your sandwich is ready!")


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
