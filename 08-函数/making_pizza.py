import pizza2  # 导入整个模块
import pizza2 as p  # 使用 as 给模块指定别名

from pizza2 import make_pizza  # 导入特定的函数
from pizza2 import make_pizza as mp  # 使用 as 给函数指定别名
from pizza2 import *  # 导入模块中的所有函数

pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
