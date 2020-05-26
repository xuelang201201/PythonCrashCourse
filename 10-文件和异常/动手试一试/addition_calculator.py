"""
加法计算器：将你为完成练习 10-6 而编写的代码放在一个 while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
"""
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("Give me a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        s = x + y
        print("The sum of %d and %d is %d." % (x, y, s))
