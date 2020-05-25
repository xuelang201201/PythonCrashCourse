"""
电瓶升级：在本节最后一个 electric_car.py 版本中，给 Battery 类添加一个名为 upgrade_battery()的方法。这个方法检查电瓶容量，
如果它不是 85，就将它设置为 85。创建一辆电瓶容量为默认值的电动汽车，调用方法 get_range()，然后对电瓶进行升级，并再次调用
get_range()。你会看到这辆汽车的续航里程增加了。
"""


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has %d miles on it." % self.odometer_reading)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# 将实例用作属性
class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a %d-kWh battery." % self.battery_size)

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        global r
        if self.battery_size == 70:
            r = 240
        elif self.battery_size == 85:
            r = 270

        message = "This car can go approximately %d miles on a full charge." % r
        print(message)

    def upgrade_battery(self):
        """电瓶升级"""
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


# 继承
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super(ElectricCar, self).__init__(make, model, year)
        # self.battery_size = 70  # 给子类定义属性
        self.battery = Battery()

    # # 给子类定义方法
    # def describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print("This car has a %d-kWh battery." % self.battery_size)

    # # 重写父类的方法
    # def fill_gas_tank(self):
    #     """电动汽车没有油箱"""
    #     print("This car doesn't need a gas tank!")


if __name__ == '__main__':
    print("Make an electric car, and check the battery:")
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()

    print("\nUpgrade the battery, and check it again:")
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()

    print("\nTry upgrading the battery a second time.")
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
