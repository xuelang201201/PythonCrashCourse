"""
词汇表2：既然你知道了如何遍历字典，现在请整理 glossary.py，将其中的一系列 print 语
句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后，再在词汇表中添加 5 个 Python
术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
"""
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
}

for word, meaning in glossary.items():
    print("%s: %s" % (word.title(), meaning))
