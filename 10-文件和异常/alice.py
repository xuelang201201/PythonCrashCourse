filename = 'alice.txt'

# 处理 FileNotFoundError 异常
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
