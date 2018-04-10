while True:
    reason = input("Why are you like programing: ")
    if reason == 'quit':
        break
    print(reason)
    with open('reasons.txt', 'a') as f:
        f.write(reason + '\n')
