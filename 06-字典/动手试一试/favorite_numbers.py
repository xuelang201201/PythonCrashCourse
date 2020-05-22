"""
喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字，并将这些名字作为字典中的键；想出每个人喜欢的一个数字，
并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
"""
favorite_numbers = {
    'edward': 1,
    'phil': 5,
    'sarah': 9,
    'jen': 6,
    'david': 7,
    'charlie': 8,
}

for name, number in favorite_numbers.items():
    print("%s's favorite number is %d." % (name.title(), number))
