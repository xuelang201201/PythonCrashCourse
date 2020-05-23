"""
10 的整数倍：让用户输入一个数字，并指出这个数字是否是 10 的整数倍。
"""
number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print("%d is a multiple of ten." % number)
else:
    print("%d is not a multiple of ten." % number)
