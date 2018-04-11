try:
    with open('text.txt') as f:
        text = f.read()
except FileNotFoundError:
    print("file not found!")
else:
    count = text.lower().count('success')
    print(count)
