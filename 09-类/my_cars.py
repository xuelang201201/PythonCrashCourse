import electric_car  # 导入整个模块

from electric_car import Car, ElectricCar  # 从一个模块中导入多个类

# my_beetle = Car('volkswagen', 'beetle', 2016)
my_beetle = electric_car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
