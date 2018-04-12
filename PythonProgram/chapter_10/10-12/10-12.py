import json


filename = 'number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Please input your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print("I know you favorite number!it's %s." % number)
