class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name)
        print("Restaurant type is " + self.restaurant_type)

    def open_restaurant(self):
        print("The restaurant is open.")
