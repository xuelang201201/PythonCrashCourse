"""修改列表元素"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles)
# ['ducati', 'yamaha', 'suzuki']

"""在列表中添加元素"""
# 1.在列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

# 2.在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
# ['ducati', 'honda', 'yamaha', 'suzuki']

"""从列表中删除元素"""
# 1.使用 del 语句删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)
# ['yamaha', 'suzuki']

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

del motorcycles[1]
print(motorcycles)
# ['honda', 'suzuki']

# 2.使用方法 pop() 删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles)
# ['honda', 'yamaha']
print(popped_motorcycle)
# suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a %s." % last_owned.title())
# The last motorcycle I owned was a Suzuki.

# 3.弹出列表中任何位置处的元素
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a %s.' % first_owned.title())
# The first motorcycle I owned was a Honda.

# 4.根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
print("\nA %s is too expensive for me." % too_expensive.title())
# A Ducati is too expensive for me.
