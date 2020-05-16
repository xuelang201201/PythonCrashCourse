"""
数字8：编写 4 个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字 8。为使用 print 语
句来显示结果，务必将这些表达式用括号括起来，也就是说，你应该编写 4 行类似于下面的代码：
_______________________________________________________________________________________
print(5 + 3)
———————————————————————————————————————————————————————————————————————————————————————
输出应为 4 行，其中每行都只包含数字 8。
"""
print(5 + 3)
print(9 - 1)
print(2 * 4)
print(56 // 7)  # // 整除

"""
最喜欢的数字：将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，
然后将这条消息打印出来。
"""
favorite_number = 7
message = "My favorite number is %d." % favorite_number
print(message)

name = input("What's your name? ")
favorite_number = input("What's your favorite number? ")
message = "%s's favorite number is %s." % (name.title(), favorite_number)
print(message)
