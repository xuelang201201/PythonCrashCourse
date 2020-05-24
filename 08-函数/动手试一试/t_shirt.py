"""
8-3 T恤：编写一个名为 make_shirt()的函数，它接受一个尺码以及要印刷到T恤上的字样。
这个函数应打印一个句子，概要说明T恤的尺码和字样。
使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数。
"""


def make_shirt(size, message):
    print("I'm going to make a %s t-shirt." % size)
    print('It will say, "%s".' % message)


make_shirt('large', 'I love Python!')
make_shirt(message="下次一定", size='medium')
