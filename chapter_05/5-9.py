name_list = []
if name_list == []:
    print("We need to find some users.")
else:
    for name in name_list:
        if name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello %s,thank you for logging in again." % name)
