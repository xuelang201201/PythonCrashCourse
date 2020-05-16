"""
计算 1~1 000 000 的总和：创建一个列表，其中包含数字 1~1 000 000，再使用 min() 和 max() 核实该列表确实是
从 1 开始，到 1 000 000 结束的。另外，对这个列表调用函数 sum()，看看 Python 将一百万个数字相加需要多长时间。
"""

numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
