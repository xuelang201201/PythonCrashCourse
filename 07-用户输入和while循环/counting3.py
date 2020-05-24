# 避免无限循环
x = 1
while x <= 5:
    print(x)
    x += 1

# 这个循环将没完没了地运行！
x = 1
while x <= 5:
    print(x)
