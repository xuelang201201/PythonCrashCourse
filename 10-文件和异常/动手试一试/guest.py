"""
访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件 guest.txt 中。
"""
with open('guest.txt', 'w') as f:
    name = input("What's your name? ")
    f.write(name)
