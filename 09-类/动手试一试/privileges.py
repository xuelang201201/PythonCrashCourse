"""
权限：编写一个名为 Privileges 的类，它只有一个属性————privileges，其中存储了练习 9-7 所说的字符串列表。将方法 show_privileges()
移到这个类中。在 Admin 类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，并使用方法 show_privileges()来显示其权限。
"""
from users import User


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super(Admin, self).__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


class Privileges:

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print('- ' + privilege)
        else:
            print("- This user has no privileges.")


if __name__ == '__main__':
    charlie = Admin('charlie', 'will', 'xuelang201201', 'xuelang201201@gmail.com', 'tokyo')
    charlie.describe_user()

    charlie.privileges.show_privileges()

    print("\nAdding privileges...")
    charlie_privileges = [
        'can add post',
        'can delete post',
        'can reset password',
    ]
    charlie.privileges.privileges = charlie_privileges
    charlie.privileges.show_privileges()
