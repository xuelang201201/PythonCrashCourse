"""
检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
1.创建一个至少包含 5 个用户名的列表，并将其命名为 current_users。
2.再创建一个包含 5 个用户名的列表，将其命名为 new_users，并确保其中有一两个用户名也包含在列表 current_users 中。
3.遍历列表 new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；
否则，打印一条消息，指出这个用户名未被使用。
4.确保比较时不区分大小写；换句话说，如果用户名 'John' 已被使用，应拒绝用户名 'JOHN'。
"""
current_users = ['sarah', 'JOhn', 'peter', 'edward', 'eric']

new_users = ['ada', 'JOHN', 'charlie', 'apple', 'Sarah']

temp_users = []
for current_user in current_users:
    temp_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in temp_users:
        print("Sorry, username '%s' has been taken! Please try another one." % new_user)
    else:
        print("Congratulations, username '%s' is available!" % new_user)
