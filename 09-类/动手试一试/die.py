"""
骰子：模块 random 包含以各种方式生成随机数的函数，其中的 randint()返回一个位于指定范围内的整数，
例如，下面的代码返回一个 1~6 内的整数：
    from random import randint
    x = randint(1, 6)
请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一个名为 roll_die()的方
法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰子，再掷 10 次。
创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次。
"""
from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x, end=' ')


if __name__ == '__main__':
    die6 = Die()
    print("6-sides die roll 10 times:")
    for _ in range(10):
        die6.roll_die()

    die10 = Die(10)
    print("\n10-sides die roll 10 times:")
    for _ in range(10):
        die10.roll_die()

    die20 = Die(20)
    print("\n20-sides die roll 10 times:")
    for _ in range(10):
        die20.roll_die()
