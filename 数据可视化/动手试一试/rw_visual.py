"""
分子运动：修改 rw_visual.py，将其中的 plt.scatter()替换为 plt.plot()。为模拟花粉在水滴表面的运动路径，
向 plt.plot()传递 rw.x_values 和 rw.y_values，并指定实参值 linewidth。使用 5000 个点而不是 50 000 个点。
"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)  # 使用 zorder 将点显示在线上面

    # 突出起点和终点
    plt.scatter(0, 0, c='green', s=75, zorder=2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=75, zorder=2)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # 模拟多次随机漫步
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
