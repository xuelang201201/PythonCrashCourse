"""
三家餐馆：根据你为完成练习 9-1 而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant()。
"""


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = "%s serves wonderful %s." % (self.name, self.cuisine_type)
        print('\n' + msg)

    def open_restaurant(self):
        msg = "%s is open. Come on in!" % self.name
        print('\n' + msg)


if __name__ == '__main__':
    mean_queen = Restaurant('the mean queen', 'pizza')
    mean_queen.describe_restaurant()

    ludvigs = Restaurant("ludvig's bistro", 'seafood')
    ludvigs.describe_restaurant()

    mango_thai = Restaurant('mango thai', 'thai food')
    mango_thai.describe_restaurant()
