"""
城市名：编写一个名为 city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
    "Santiago, Chile"
至少使用三个城市-国家对调用这个函数，并打印它返回的值。
"""


def city_country(city, country):
    return '%s, %s' % (city.title(), country.title())


c = city_country('santiago', 'chile')
print(c)

c = city_country('paris', 'france')
print(c)

c = city_country('tokyo', 'japan')
print(c)
