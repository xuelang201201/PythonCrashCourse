"""列表操作"""
"""
嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请那些人？请创建
一个列表，其中包含至少 3 个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
"""
names = ['ada lovelace', 'albert einstein', 'peter pan', 'jack sparrow', 'monkey d luffy']
for name in names:
    print("%s, would you like to have dinner with me tonight?" % name.title())

"""
修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
1.以完成上面编写的程序为基础，在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
2.修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
3.再次打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
print("%s can't come tonight." % names[0].title())
names[0] = 'nikola tesla'
for name in names:
    print("%s, would you like to have dinner with me tonight?" % name.title())

"""
添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
1.以完成上面编写的程序为基础，在程序末尾添加一条 print 语句，指出你找到了一个更大的餐桌。
2.使用 insert()将一位新嘉宾添加到名单开头。
3.使用 insert()将另一位新嘉宾添加到名单中间。
4.使用 append()将最后一位新嘉宾添加到名单末尾。
5.打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
print("Good news, I found a larger table.")
names.insert(0, 'bob dylan')
names.insert(3, 'johnny depp')
names.append('jackie chan')
for name in names:
    print("%s, would you like to have dinner with me tonight?" % name.title())

"""
缩减嘉宾：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
1.以完成上面编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
2.使用 pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一
条消息，让嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
3.对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀请之列。
4.使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
"""
# 1
print('I can only invite two guests.')

# 2
popped_names = []
while len(names) > 2:
    popped_name = names.pop()
    popped_names.append(popped_name)

for name in popped_names:
    print("%s, sorry you can't come tonight." % name.title())

# 3
for name in names:
    print("%s, would you like to have dinner with me tonight?" % name.title())

# 4
while len(names) > 0:
    del names[0]

print(names)

