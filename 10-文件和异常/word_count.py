def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file %s does not exist." % filename
        print(msg)
    else:
        # 计算文件大致包含多少单词
        words = contents.split()
        num_words = len(words)
        print("The file %s has about %d words." % (filename, num_words))


if __name__ == '__main__':
    # 单个文件
    file_name = 'alice.txt'
    count_words(file_name)

    # 多个文件
    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
    for filename in filenames:
        count_words(filename)
