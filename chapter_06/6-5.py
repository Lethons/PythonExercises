rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'huanghe': 'china'
}
for key, value in rivers.items():
    print("The %s run through %s." % (key.title(), value.title()))

for k in rivers.keys():
    print(k.title())

for v in rivers.values():
    print(v.title())
