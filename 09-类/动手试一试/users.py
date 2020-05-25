"""
用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的
其他几个属性。在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；再定义一个
名为 greet_user()的方法，它向用户发出个性化的问候。
创建多个表示不同用户的示例，并对每个实例都调用上述两个方法。
"""


class User:

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print("\n%s %s" % (self.first_name, self.last_name))
        print("  Username: %s" % self.username)
        print("  Email: %s" % self.email)
        print("  Location: %s" % self.location)

    def greet_user(self):
        print("Welcome come back, %s!" % self.username)


if __name__ == '__main__':
    eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
    eric.describe_user()
    eric.greet_user()

    charlie = User('charlie', 'will', 'xuelang201201', 'xuelang201201@gmail.com', 'tokyo')
    charlie.describe_user()
    charlie.greet_user()
