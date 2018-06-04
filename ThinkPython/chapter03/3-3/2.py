def print_1(x):
    for i in range(x):
        print('+ - - - -', end=' ')
    print('+')

def print_2(x):
    for i in range(3):
        for i in range(x):
            print('|        ', end=' ')
        print('|')

def print_table(f1, f2, x, y):
    f1(x)
    for i in range(y):
        f2(x)
        f1(x)

print_table(print_1, print_2, 4, 4)