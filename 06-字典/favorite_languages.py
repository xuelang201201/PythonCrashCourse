favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# print("Sarah's favorite language is %s." % favorite_languages['sarah'].title())
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
