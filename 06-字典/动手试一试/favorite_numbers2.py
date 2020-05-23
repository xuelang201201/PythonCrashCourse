"""
喜欢的数字：修改为完成练习 6-2 而编写的程序，让每个都可以有
多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
"""
favorite_numbers = {
    'edward': [1, 2, 3],
    'phil': [5],
    'sarah': [9, 1],
    'jen': [6, 8, 10, 99],
    'david': [7, 24, 100, 0, 4],
    'charlie': [8],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print("%s's favorite numbers are:" % name.title())
    else:
        print("%s's favorite number is:" % name.title())
    for number in numbers:
        print(' ', number)
