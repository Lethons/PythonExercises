def city_county(name, county):
    ret = name.title() + ',' + county.title()
    return ret


print(city_county('wuhu', 'china'))
print(city_county('santiago', 'chile'))
print(city_county('new york', 'usa'))
