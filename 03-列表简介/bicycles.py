"""列表是什么：列表是由一系列按特定顺序排列的元素组成"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# ['trek', 'cannondale', 'redline', 'specialized']

# 访问列表元素
print(bicycles[0])
# trek
print(bicycles[-1].title())  # 访问列表最后一个元素
# Specialized

# 索引从0而不是1开始
print(bicycles[1])
# cannondale
print(bicycles[3])
# specialized

# 使用列表中的各个值
message = "My first bicycle was a %s." % bicycles[0].title()

print(message)
# My first bicycle was a Trek.
