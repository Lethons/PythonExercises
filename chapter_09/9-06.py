class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name: " + self.restaurant_name)
        print("Restaurant type: " + self.restaurant_type)
        print("Number served: " + str(self.number_served))

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number):
        self.number_served = number
        print("Set number served: " + str(self.number_served))

    def increment_number_seved(self, nums):
        self.number_served += nums


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['apple icecream', 'banana icecream', 'organe icecream']

    def print_flavors(self):
        print(self.flavors)


IceCreamStand = IceCreamStand('HiIce', 'icecream')
IceCreamStand.print_flavors()
IceCreamStand.describe_restaurant()
