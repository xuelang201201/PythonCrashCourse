import csv

from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取日期、最高气温和最低气温
filename = 'sitka_weather_2014.csv'
# filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    # 分析CSV文件头
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # 打印文件头及其位置
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件中获取日期和最高气温
    # highs = []
    # dates, highs = [], []
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

    # print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(highs, c='red')
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')

    # 设置图形的格式
    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    # plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 绘制斜的日期标签
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
