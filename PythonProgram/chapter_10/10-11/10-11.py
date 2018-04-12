import json


favorite_num = input("Please input your favirite number: ")
with open('number.json', 'w') as f:
    json.dump(favorite_num, f)

with open('number.json', 'r') as f:
    number = json.load(f)

print("I know your favorite number!It's " + number + '.')
