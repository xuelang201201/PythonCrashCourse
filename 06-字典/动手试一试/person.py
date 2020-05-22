"""
人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含
键 first_name、last_name、age 和 city。将存储在该字典中的每项信息都打印出来。
"""
person = {
    'first_name': 'edward',
    'last_name': 'weevil',
    'age': 28,
    'city': 'berlin',
}

full_name = person['first_name'] + ' ' + person['last_name']

print("%s is %d years old, and came from %s." % (full_name.title(), person['age'], person['city'].title()))
