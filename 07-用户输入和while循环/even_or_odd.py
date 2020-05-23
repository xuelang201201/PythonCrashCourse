# 求模运算符
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number %d is even." % number)
else:
    print("\nThe number %d is odd." % number)
