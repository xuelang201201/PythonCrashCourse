import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    # 分析CSV文件头
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
