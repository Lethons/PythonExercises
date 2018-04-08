age = ""
while age != 'quit':
    age = input("How old are you?")
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("You are free!")
        elif age < 12:
            print("You need spend 10$.")
        else:
            print("You need spend 15$.")
