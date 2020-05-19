"""
喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的 if 语句，检查列表中是否包含特定的水果。
1.将该列表命名为 favorite_fruits，并在其中包含三种水果。
2.编写 5 条 if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如 “You really like bananas!”。
"""

favorite_fruits = ['apple', 'banana', 'orange']

fruits = ['strawberry', 'pineapple', 'apple', 'banana', 'orange']

for fruit in fruits:
    if fruit in favorite_fruits:
        print("You really like %ss!" % fruit)
