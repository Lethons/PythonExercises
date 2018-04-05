cities = {
    'beijing': {
        'country': 'china',
        'population': 123456789,
        'acreage': 123456,
    },
    'tianjin': {
        'country': 'china',
        'population': 321456987,
        'acreage': 135246,
    },
    'nanjing': {
        'country': 'china',
        'population': 123456987,
        'acreage': 123654,
    },
}
for city, information in cities.items():
    print("%s: " % city)
    for k, v in information.items():
        print(k + ":" + str(v))
