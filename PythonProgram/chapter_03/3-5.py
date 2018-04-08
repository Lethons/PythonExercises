name_lists = ['Susan', 'Leo', 'Jack']
for name in name_lists:
    print('I want to invite ' + name)
print(name_lists[0] + " can't come.")
name_lists[0] = 'Mark'
for name in name_lists:
    print('I want to invite ' + name)
