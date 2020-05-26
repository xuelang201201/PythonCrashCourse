"""
C语言学习笔记：可使用方法 replace()将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例，演示了如何将
句子中的'dog'替换为'cat'：
    >>> message = "I really like dogs."
    >>> message.replace('dog', 'cat')
    'I really like cats.'

读取你刚创建的文件 learning_python.txt 中的每一行，将其中的 Python 都替换为另一门语言的名称，如 C。将修改后
的各行都打印到屏幕上。
"""
filename = 'learning_python.txt'
new_lines = []
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        new_lines.append(line.replace('Python', 'C'))

for line in new_lines:
    print(line.strip())
