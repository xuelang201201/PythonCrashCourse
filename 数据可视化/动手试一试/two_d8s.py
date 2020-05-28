"""
两个 D8 骰子：请模拟同事掷两个 8 面骰子 1000 次的结果。逐渐增加掷骰子的次数，直到系统不堪重负位置。
"""
import pygal

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for roll_num in range(1000000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1,000,000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('two_d8s.svg')
