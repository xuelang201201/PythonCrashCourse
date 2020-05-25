"""
冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，让它继承你为完成练习 9-1 或练习 9-4 而
编写的 Restaurant 类。这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为 flavors 的属性，用
于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个 IceCreamStand 实例，并调用这个方法。
"""
from restaurant2 import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        super(IceCreamStand, self).__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


if __name__ == '__main__':
    big_one = IceCreamStand('The Big One')
    big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

    big_one.describe_restaurant()
    big_one.show_flavors()
