favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
name_list = ['leo', 'jen', 'jack', 'phil']
for name in name_list:
    if name in favorite_languages.keys():
        print("Thanks for your join.")
    else:
        print("I'd like to invite you to participate in the investigation.")
