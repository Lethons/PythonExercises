class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name)
        print("Restaurant type is " + self.restaurant_type)

    def open_restaurant(self):
        print("The restaurant is open.")


restaurant1 = Restaurant('Michelin', 'fivestar hotel')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('KFC', 'fastfood')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('MacDonald', 'fastfood')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
