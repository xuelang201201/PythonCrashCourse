# 处理 ZeroDivisionError 异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
