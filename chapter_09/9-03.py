class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("first_name: " + self.first_name)
        print("last_name: " + self.last_name)
        print("age: " + str(self.age))

    def greet_user(self):
        print("Hello " + self.first_name.title())


user1 = User('jack', 'brown', 22)
user1.describe_user()
user1.greet_user()

user2 = User('alice', 'kait', 23)
user2.describe_user()
user2.greet_user()
