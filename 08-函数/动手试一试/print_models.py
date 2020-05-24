"""
打印模型：将示例 print_models.py 中的函数放在另一个名为 printing_functions.py 的文件中；在 print_models.py 的开
头编写一条 import 语句，并修改这个文件以使用导入的函数。
"""

from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
