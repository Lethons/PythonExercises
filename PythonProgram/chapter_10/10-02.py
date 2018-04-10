with open('learning_python.txt', 'r') as f:
    text = f.read()
    rep = text.replace('Python', 'C')
    print(rep)
