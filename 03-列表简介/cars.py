# 使用方法 sort() 对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)  # 按字母顺序相反的顺序打印列表
print(cars)
# ['toyota', 'subaru', 'bmw', 'audi']

# 使用函数 sorted() 对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
# Here is the original list:
# ['bmw', 'audi', 'toyota', 'subaru']
#
# Here is the sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']
#
# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']

# 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)
# ['subaru', 'toyota', 'audi', 'bmw']

# 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
# 4
