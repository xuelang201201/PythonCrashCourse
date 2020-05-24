"""
不变的魔术师：修改你为完成练习 8-10 而编写的程序，在调用函数 make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，
请返回修改后的列表，并将其存储到另一个列表中。分别使用这两个列表来调用 show_magicians()，确认一个列表包含的是原来的魔术师名
字，而另一个列表包含的是添加了字样 “the Great” 的魔术师名字。
"""


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians


magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)
