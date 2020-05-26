"""
沉默的猫和狗：修改你在练习 10-8 中编写的 except 代码块，让程序在文件不存在时一言不发。
"""
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        # print("  Sorry, I can't find that file.")
        pass
