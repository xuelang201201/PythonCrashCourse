"""
更多的条件测试：你并非只能创建 10 个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加
入到 conditional_tests.py 中。对于下面列出的各种测试，至少编写一个结果为 True 和 False 的测试。
1.检查两个字符串相等和不等。
2.使用函数 lower()的测试。
3.检查两个数字相等、不等、大于、小于、大于等于和小于等于。
4.使用关键字 and 和 or 的测试。
5.测试特定的值是否包含在列表中。
6.测试特定的值是否未包含在列表中。
"""
language = 'python'
print("Is language == 'python'? I predict True.")
print(language == 'python')
print("\nIs language == 'go'? I predict False.")
print(language == 'go')

name = 'Sarah'
print("\nIs name == 'sarah'? I predict True.")
print(name.lower() == 'sarah')
print("\nIs name == 'Sarah'? I predict False.")
print(name == 'sarah')

age = 23
print("\nIs age == 23? I predict True.")
print(age == 23)
print("\nIs age != 23? I predict False.")
print(age != 23)

print("\nIs age > 22? I predict True.")
print(age > 22)
print("\nIs age < 22? I predict False.")
print(age < 22)

print("\nIs age >= 23? I predict True.")
print(age >= 23)
print("\nIs age <= 22? I predict False.")
print(age <= 22)

print("\nIs language = 'python' or age = 24? I predict True.")
print(language == 'python' or age == 24)
print("\nIs language = 'python' and age = 24? I predict False.")
print(language == 'python' and age == 24)

colors = ['red', 'blue', 'white', 'black', 'yellow']
print("\nIs 'red' in colors? I predict True.")
print('red' in colors)
print("\nIs 'green' in colors? I predict False.")
print('green' in colors)

print("\nIs 'purple' not in colors? I predict True.")
print('purple' not in colors)
print("\nIs 'black' not in colors? I predict False.")
print('black' not in colors)
