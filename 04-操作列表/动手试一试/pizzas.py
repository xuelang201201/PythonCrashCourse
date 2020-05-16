"""
比萨：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用 for 循环将每种比萨的名称都打印出来。
1.修改这个 for 循环，使其打印包含比萨名称的句子，而仅仅是比萨的名称。对于每种比萨，都显示一行输出，
如 “I like pepperoni pizza”。
2.在程序末尾添加一行代码，它不在 for 循环中，指出你有多喜欢比萨。输出应该包含针对每种比萨的消息，还有
一个总结性的句子，如 “I really love pizza!”。
"""
pizzas = ['pepperoni', 'bacon', 'cheese']
for pizza in pizzas:
    print("I like %s pizza." % pizza)

print("I really love pizza!")
