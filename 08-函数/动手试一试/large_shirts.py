"""
大号T恤：修改函数 make_shirt()，使其在默认情况下制作一件印有字样 “I love Python” 的大号T恤。调用这个函数来制作如下T恤：
一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。
"""


def make_shirt(size='large', message='I love Python!'):
    print("I'm going to make a %s t-shirt." % size)
    print('It will say, "%s".' % message)


make_shirt()
make_shirt(size='medium')
make_shirt(message='I love Go, too!')

