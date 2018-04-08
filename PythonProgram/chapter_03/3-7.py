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
print("The big table can't be delivered, so I can only invite two people.")
for i in range(0, len(name_lists)-2):
    pop_name = name_lists.pop()
    print("sorry,I can't invite you", pop_name)
for name in name_lists:
    print('I want to invite ' + name)
while name_lists:
    del name_lists[0]
print(name_lists)
