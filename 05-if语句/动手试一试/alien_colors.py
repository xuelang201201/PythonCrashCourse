"""
外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为 alien_color 的变量，并将其设置为 'green'、'yellow'或'red'。
1.编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了 5 个点。
2.编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
"""
alien_color = 'green'

if alien_color == 'green':
    points = 5
    print("You got %d points." % points)

"""
外星人颜色#2：编写一个if-else结构。
1.如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 个点。
2.如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10 个点。
3.编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块。
"""
alien_color = 'red'

if alien_color == 'green':
    points = 5
else:
    points = 10
print("You got %d points." % points)

"""
外星人颜色#3：if-elif-else 结构。
1.如果外星人是绿色的，就打印一条消息，指出玩家获得了 5 个点。
2.如果外星人是黄色的，就打印一条消息，指出玩家获得了 10 个点。
3.如果外星人是红色的，就打印一条消息，指出玩家获得了 15 个点。
4.编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
"""
alien_color = 'red'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print("You got %d points." % points)
