favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n%s's favorite languages are:" % name.title())
    else:
        print("\n%s's favorite language is:" % name.title())
    for language in languages:
        print("\t", language.title())
