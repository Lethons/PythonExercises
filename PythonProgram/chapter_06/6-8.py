lulu = {'susan': 'pig'}
lucy = {'alice': 'cat'}
momo = {'jack': 'dog'}
pets = [lulu, lucy, momo]
for pet in pets:
    for k, v in pet.items():
        print(k + ':' + v)
