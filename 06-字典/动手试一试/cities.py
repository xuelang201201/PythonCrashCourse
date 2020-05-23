"""
城市：创建一个名为 cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，并在其中包含该城市所属的
国家、人口约数以及一个有关该城市的事实。在表示每座城市的字典中，应包含 country、population 和 fact 等键。将每座
城市的名字及有关它们的信息都打印出来。
"""
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himalaya',
    }
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n%s is in %s." % (city.title(), country))
    print(' It has a population of about %d.' % population)
    print(' The %s mountains are nearby.' % mountains)
