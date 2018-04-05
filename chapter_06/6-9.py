favorite_places = {
    'susan': ['huangshan', 'beijing'],
    'alice': ['tianjin'],
    'jack': ['hangzhou', 'nanjin', 'sichuang'],
}
for name, places in favorite_places.items():
    print("%s's favorite place is: " % name)
    for place in places:
        print(place)
