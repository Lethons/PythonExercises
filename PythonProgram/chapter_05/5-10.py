current_users = ['Admin', 'Leo', 'Susan', 'Jack', 'Mark']
new_users = ['Alice', 'TOM', 'LEO', 'jack', 'lucy']
ls = []
for name in current_users:
    ls.append(name.lower())
for new_user in new_users:
    if new_user.lower() in ls:
        print("you need to input other username.")
    else:
        print("this username is not used.")
