favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
favorite_languages['jack'] = 'c#'
for name, language in favorite_languages.items():
    print("%s's favorite language is %s." % (name, language))
