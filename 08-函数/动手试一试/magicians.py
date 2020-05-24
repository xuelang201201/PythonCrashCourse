"""
魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为 show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
"""


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)
