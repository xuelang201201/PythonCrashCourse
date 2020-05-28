import csv

from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取日期、最高气温和最低气温
filename = 'death_valley_2014.csv'
# filename = 'sitka_weather_2014.csv'
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
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(highs, c='red')
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    # plt.title("Daily high temperatures - 2014", fontsize=24)
    # plt.title("Daily high and low temperatures - 2014", fontsize=24)
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 绘制斜的日期标签
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # 让x轴顶格
    plt.xlim(min(dates), max(dates))

    plt.show()
