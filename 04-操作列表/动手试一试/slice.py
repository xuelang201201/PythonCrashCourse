"""
切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
1.打印消息 “The first three items in the list are:”，再使用切片来打印列表的前三个元素。
2.打印消息 “Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
3.打印消息 “The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
"""
odds = list(range(1, 22, 2))
print(odds)

print("The first three items in the list are:")
for odd in odds[:3]:
    print(odd)

print("Three items from the middle of the list are:")
for odd in odds[4:7]:
    print(odd)

print("The last three items in the list are:")
for odd in odds[-3:]:
    print(odd)

