"""
以特殊方式跟管理员打招呼：创建一个至少包含 5 个用户名的列表，且其中一个用户名为 'admin'。想象你要编写代码，
在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条消息。
1.如果用户名为 'admin'，就打印一条特殊的问候消息，如 “Hello admin, would you like to see a status report?”
2.否则，打印一条普通的问候消息，如 “Hello Eric, thank you for logging in again.”。
"""

# users = ['eric', 'john', 'admin', 'sarah', 'peter']

"""
处理没有用户的情形：在为完成上面编写的程序中，添加一条 if 语句，检查用户名列表是否为空。
1.如果为空，就打印消息 “We need to find some users!”。
2.删除列表中的所有用户名，确定将打印正确的消息。
"""
users = []


if len(users) == 0:
    print("We need to find some users!")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello %s, thank you for logging in again." % user.title())
