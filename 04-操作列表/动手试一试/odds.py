"""
奇数：通过给函数 range()指定第三个参数来创建一个列表，其中
包含 1~20 的奇数；在使用一个 for 循环将这些数字都打印出来。
"""
odds = list(range(1, 20, 2))
for odd in odds:
    print(odd)
