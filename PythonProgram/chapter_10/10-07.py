while True:
    try:
        num1 = input("Please input first number: ")
        if num1 == 'quit':
            break
        num2 = input("Please input secend number: ")
        if num2 == 'quit':
            break
        num1 = int(num1)
        num2 = int(num2)
        sum = num1 + num2
    except ValueError:
        print(ValueError)
    else:
        print(sum)
