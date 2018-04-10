while True:
    name = input("Please input your name: ")
    if name == 'quit':
        break
    print("Nice to meet you %s." % name.title())
    with open('guest_book.txt', 'a') as f:
        f.write(name.title() + '\n')
