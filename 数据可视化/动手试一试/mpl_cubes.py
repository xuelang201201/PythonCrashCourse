"""
立方：数字的三次方被成为其立方。请绘制一个图形，显示前 5 个
整数的立方值，再绘制一个图像，显示前 5000 个整数的立方值。
"""
import matplotlib.pyplot as plt


def first_5():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 8, 27, 64, 125]
    plt.scatter(x_values, y_values, s=40)
    plt.title("Cubes", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Cube of Value", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()


def first_5000():
    x_values = list(range(1, 5001))
    y_values = [x ** 3 for x in x_values]
    plt.scatter(x_values, y_values, s=40)
    # 设置图表标题并给坐标轴加上标签
    plt.title("Cubes", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Cube of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置每个坐标轴的取值范围
    plt.axis([0, 5100, 0, 5100 ** 3])
    plt.show()


if __name__ == '__main__':
    first_5()
    first_5000()
