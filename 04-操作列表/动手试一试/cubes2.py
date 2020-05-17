"""
立方解析：使用列表解析生成一个列表，其中包含前 10 个整数的立方。
"""

cubes = [number ** 3 for number in range(1, 11)]
for cube in cubes:
    print(cube)
