"""
五香烟熏牛肉（pastrami）卖完了：使用为完成练习 7-8 而创建的列表 sandwich_orders，并确保 'pastrami' 在其中至少出现了三次。
在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个 while 循环将列表 sandwich_orders 中
的 'pastrami' 都删除。确认最终的列表 finished_sandwiches 中不包含 'pastrami'。
"""
sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print()
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your %s sandwich." % current_sandwich)
    finished_sandwiches.append(current_sandwich)

print()
for sandwich in finished_sandwiches:
    print("I made you %s sandwich." % sandwich)
