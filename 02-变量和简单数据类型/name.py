"""使用方法修改字符串的大小写"""
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

"""合并（拼接）字符串"""
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
print("Hello, %s!" % full_name.title())

message = "Hello, " + full_name.title() + "!"
print(message)
