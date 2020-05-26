import json


def get_sorted_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出名字"""
    username = get_sorted_username()
    if username:
        print("Welcome back, %s!" % username)
    else:
        username = get_new_username()
        print("We'll remember you when you come back, %s!" % username)


if __name__ == '__main__':
    greet_user()
