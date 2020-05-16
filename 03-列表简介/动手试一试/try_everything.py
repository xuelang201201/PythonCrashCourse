"""
尝试使用各个函数：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一
个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
"""
things = ['himalaya', 'yangtze', 'iceland', 'barcelona', 'python', 'jackie chan']
# 访问列表元素
print('My favorite actor is %s.' % things[-1].title())

# 修改列表元素
things[1] = 'amazon'
print(things)

# 在列表末尾添加元素
things.append('one piece')
print(things)

# 在列表中插入元素
things.insert(0, 'toyota')
print(things)

# 使用函数 sorted()对列表进行临时排序
print(sorted(things))

# 使用del语句删除元素
del things[3]
print(things)

# 使用方法pop()删除元素
popped_thing = things.pop()
print("My favorite animation is %s." % popped_thing.title())

# 弹出列表中任何位置处的元素
things.pop(0)
print(things)

# 根据值删除元素
things.remove('python')
print(things)

# 使用方法 sort()对列表进行永久性排序
things.sort()
print(things)

things.sort(reverse=True)
print(things)

things.reverse()
print(things)

print(len(things))
