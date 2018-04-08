name_lists = ['Susan', 'Leo', 'Jack']
for name in name_lists:
    print('I want to invite ' + name)
print(name_lists[0] + " can't come.")
name_lists[0] = 'Mark'
for name in name_lists:
    print('I want to invite ' + name)
print('I found a bigger table.')
name_lists.insert(0, 'Tony')
name_lists.insert(2, 'Alice')
name_lists.append('Blank')
for name in name_lists:
    print('I want to invite ' + name)
