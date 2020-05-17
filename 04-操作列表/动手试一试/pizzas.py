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

"""
你的比萨和我的比萨：创建上面比萨列表的副本，并将其存储到变量 friend_pizzas 中，再完成如下任务。
1.在原来的比萨列表中添加一种比萨。
2.在列表 friend_pizzas 中添加另一种比萨。
3.核实你有两个不同的列表。为此，打印消息 “My favorite pizzas are:”，再使用一个 for 循环来打印第
一个列表；打印消息 “My friend's favorite pizzas are:”，再使用一个 for 循环来打印第二个列表。核
实新增的比萨被添加到了正确的列表中。
"""
friend_pizzas = pizzas[:]

pizzas.append('hawaii')
friend_pizzas.append('seafood')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
