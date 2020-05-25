"""
管理员：管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承你为完成练习 9-3 或 练习 9-5 而编写的 User 类。添加一个名为
privileges 的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。编写一个名为
show_privileges()的方法，它显示管理员的权限。创建一个 Admin 实例，并调用这个方法。
"""

from users import User


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super(Admin, self).__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print('- ' + privilege)


if __name__ == '__main__':
    charlie = Admin('charlie', 'will', 'xuelang201201', 'xuelang201201@gmail.com', 'tokyo')
    charlie.describe_user()

    charlie.privileges = [
        'can add post',
        'can delete post',
        'can ban user',
    ]
    charlie.show_privileges()
