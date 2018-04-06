active = True
while active:
    message = input("Please input what you want: ")
    if message == 'quit':
        # active = False
        break
    else:
        print("We will add %s." % message)
