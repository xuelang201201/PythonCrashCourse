"""
记住喜欢的数字：将练习 10-11 中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字
并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
"""
import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks! I'll remember that.")
else:
    print("I know your favorite number! It's %s." % number)
