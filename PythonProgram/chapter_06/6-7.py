leo_dict = {
    'first_name': 'lethons',
    'last_name': 'leo',
    'age': 24,
    'city': 'wuhu',
}
jack_dict = {
    'first_name': 'jason',
    'last_name': 'jack',
    'age': 20,
    'city': 'shanghai',
}
alice_dict = {
    'first_name': 'susan',
    'last_name': 'alice',
    'age': 22,
    'city': 'nanjing',
}
people = [leo_dict, jack_dict, alice_dict]
for person in people:
    for k, v in person.items():
        print(k + ':' + str(v))
