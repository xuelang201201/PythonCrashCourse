"""
人生的不同阶段：设置变量 age 的值，再编写一个 if-elif-else 结构，根据 age 的值判断处于人生的哪个阶段。
1.如果一个人的年龄小于 2 岁，就打印一条消息，指出他是婴儿。
2.如果一个人的年龄为 2（含）~ 4 岁，就打印一条消息，指出他正蹒跚学步。
3.如果一个人的年龄为 4（含）~ 13 岁，就打印一条消息，指出他是儿童。
4.如果一个人的年龄为 13（含）~ 20 岁，就打印一条消息，指出他是青少年。
5.如果一个人的年龄为 20（含）~ 65 岁，就打印一条消息，指出他是成年人。
6.如果一个人的年龄超过 65（含）岁，就打印一条消息，指出他是老年人。
"""

stage = ''
try:
    age = int(input("How old are you? "))
    if age < 0 or age > 180:
        print("Please input a correct age.")
    else:
        if age < 2:
            stage = 'baby'
        elif age < 4:
            stage = 'toddler'
        elif age < 13:
            stage = 'children'
        elif age < 20:
            stage = 'teenager'
        elif age < 65:
            stage = 'adult'
        else:
            stage = 'senior'

        print("You are at the stage of %s." % stage)

except ValueError:
    print("Please input a correct age.")
