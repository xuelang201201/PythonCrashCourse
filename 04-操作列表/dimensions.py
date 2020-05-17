"""元组"""

# 定义元祖
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# 修改元组变量
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
