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

    # 重写父类的方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    # my_tesla.describe_battery()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
