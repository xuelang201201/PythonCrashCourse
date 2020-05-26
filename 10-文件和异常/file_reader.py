def read_file():
    """读取整个文件"""

    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents.rstrip())


def read_by_line():
    """逐行读取"""

    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())


def read_lines():
    """创建一个包含文件各行内容的列表"""

    filename = 'pi_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()
    
    for line in lines:
        print(line.rstrip())


if __name__ == '__main__':
    read_file()
    read_by_line()
    read_lines()
