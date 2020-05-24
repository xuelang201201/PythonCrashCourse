"""
汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
这样调用这个函数：提供必不可少的信息，以及两个名称-值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
    car = make_car('subaru', 'outback', color='blue', two_package=True)
打印返回的字典，确认正确地处理了所有的信息。
"""


def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }

    for option, value in options.items():
        car_dict[option] = value

    return car_dict


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)
my_accord = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(my_accord)
