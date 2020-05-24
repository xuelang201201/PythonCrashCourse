"""
了不起的魔术师：在你为完成练习 8-9 而编写的程序中，编写一个名为 make_great()的函数，对魔术师列表进行修改，在每个
魔术师进行修改，在每个魔术师的名字中都加入字样 “the Great”。调用函数 show_magicians()，确认魔术师列表确实变了。
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


magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print()
make_great(magicians)
show_magicians(magicians)
