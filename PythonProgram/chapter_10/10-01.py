with open('learning_python.txt', 'r') as f:
    text = f.read()
    print(text)

with open('learning_python.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

with open('learning_python.txt', 'r') as f:
    for line in f.readlines():
        print(line.rstrip())
