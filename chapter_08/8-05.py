def describe_city(name, county='china'):
    print("%s is in %s." % (name.title(), county.title()))


describe_city('wuhu')
describe_city('beijing')
describe_city('reykjavik', 'iceland')
