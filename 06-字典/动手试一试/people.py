"""
人：在完成练习 6-1 而编写的程序 person.py 中，再创建两个表示人的字典，然后将这三个字
典都存储在一个名为 people 的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
"""
wedward = {
    'first_name': 'edward',
    'last_name': 'weevil',
    'age': 28,
    'city': 'berlin',
}

jphil = {
    'first_name': 'phil',
    'last_name': 'jordan',
    'age': 32,
    'city': 'new york',
}

bsarah = {
    'first_name': 'sarah',
    'last_name': 'brown',
    'age': 54,
    'city': 'london',
}

people = [wedward, jphil, bsarah]

for person in people:
    full_name = person['first_name'] + ' ' + person['last_name']
    print("\nFull name: ", full_name.title())
    print("Age: ", person['age'])
    print("City: ", person['city'].title())
