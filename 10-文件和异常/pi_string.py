def use_file_content():
    """使用文件的内容"""
    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))


def million_digits_file():
    """包含一百万位的大型文件"""
    filename = 'pi_million_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string[:52] + "...")
    print(len(pi_string))


def pi_birthday():
    """圆周率值中包含你的生日吗"""
    filename = 'pi_million_digits.txt'

    with open(filename) as f:
        lines = f.readlines()
        pi_string = ''
        for line in lines:
            pi_string += line.strip()

    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")


if __name__ == '__main__':
    use_file_content()
    million_digits_file()
    pi_birthday()
