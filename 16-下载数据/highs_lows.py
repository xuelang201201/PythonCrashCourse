import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    # 分析CSV文件头
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # 打印文件头及其位置
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 从文件中获取最高气温
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)
