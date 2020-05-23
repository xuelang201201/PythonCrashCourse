"""
喜欢的地方：创建一个名为 favorite_places 的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，
都存储他喜欢的 1~3 个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
"""

favorite_places = {
    'jen': ['barcelona', 'egypt', 'hawaii'],
    'peter': ['iceland'],
    'elizabeth': ['shanghai', 'tokyo'],
}

for name, places in favorite_places.items():
    if len(places) < 2:
        print("\n%s's favorite place is:" % name.title())
    else:
        print("\n%s's favorite places are:" % name.title())

    for place in places:
        print(' ', place.title())
