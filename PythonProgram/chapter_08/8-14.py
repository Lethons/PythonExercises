def car_info(manufacturer, type, **info):
    car = {}
    car['manufacturer'] = manufacturer
    car['type'] = type
    for key, value in info.items():
        car[key] = value
    return car


car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
