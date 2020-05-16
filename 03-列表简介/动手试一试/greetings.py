"""
问候语：继续使用上面的列表，但不打印每个朋友的姓名，而为每人打印一条消息。
每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
"""
greeting = "%s, would you like to learn some Python today?"

for name in names:
    print(greeting % name.title())
