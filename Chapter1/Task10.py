class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def greet_user(self):
        print(f"Welcome back {self.username}!")

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}\n"
              f"Username: {self.username}\n"
              f"Email: {self.email}\n"
              f"Location: {self.location}")

