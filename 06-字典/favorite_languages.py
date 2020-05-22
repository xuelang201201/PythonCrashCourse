favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# print("Sarah's favorite language is %s." % favorite_languages['sarah'].title())
# 遍历字典中的所有键-值对
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print("%s, thank you for taking the poll." % name.title())

# 遍历字典中的所有值
print("The following languages have been mentioned:")
# for language in favorite_languages.values():
for language in set(favorite_languages.values()):  # 避免重复
    print(language.title())
