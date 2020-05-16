"""
个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应
非常简单，如 “Hello Eric, would you like to learn some Python today?”
"""
username = 'Eric'
message = 'Hello %s, would you like to learn some Python today?' % username
print(message)

"""
调整名字的大小写：将一个名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
"""
name = 'ada lovelace'
print(name.lower())
print(name.upper())
print(name.title())

"""
名言：找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似与下面这样（包括引号）：
Albert Einstein once said, "A person who never made a mistake never tried anything new."
"""
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

"""
名言2：重复上一个练习，但将名人的姓名存储在变量 famous_person 中，再创建要
显示的消息，并将其存储变量 message 中，然后打印这条消息。
"""
famous_person = 'albert einstein'
saying = 'A person who never made a mistake never tried anything new.'
message = '%s once said, "%s"' % (famous_person.title(), saying)
print(message)

"""
剔除人名中的空白：存储在一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合 "\t" 和 "\n" 各一次。
打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数 lstrip()、rstrip() 和 strip() 对人名进行处理，并将结果打印出来。
"""
name = '\n\n\tada lovelace\t\t\n'
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
