def print_name(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.rstrip())


filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'
print_name(filename_1)
print_name(filename_2)
