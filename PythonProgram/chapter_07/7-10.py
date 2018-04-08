place_list = []
while True:
    place = input(
        "If you could visit one place in the world, where would you go?")
    if place == 'quit':
        break
    place_list.append(place)
print(place_list)
