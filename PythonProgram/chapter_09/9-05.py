class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attemps = 0

    def describe_user(self):
        print("first_name: " + self.first_name)
        print("last_name: " + self.last_name)
        print("age: " + str(self.age))
        print("login attemps: " + str(self.login_attemps))

    def greet_user(self):
        print("Hello " + self.first_name.title())

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0


user = User('jack', 'mark', 22)
user.describe_user()
print("-" * 50)
user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()
user.describe_user()
print("-" * 50)
user.reset_login_attemps()
user.describe_user()
