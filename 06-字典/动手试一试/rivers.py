"""
河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键-值对可能是'nile': 'egypt'。
1.使用循环为每条河流打印一条消息，如 “The Nile runs through Egypt.”。
2.使用循环将该字典中每条河流的名字都打印出来。
3.使用循环将该字典包含的每个国家的名字都打印出来。
"""
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print("The %s runs through %s." % (river.title(), country.title()))
