"""
访客名单：编写一个 while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加
到文件 guest_book.txt 中。确保这个文件中的每条记录都独占一行。
"""
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("What's your name? ")
    if name == 'quit':
        break
    with open(filename, 'a') as f:
        f.write(name + '\n')
        print("Hi %s, you've been added to the guest book." % name)
