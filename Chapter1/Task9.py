class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def name(self):
        return self.name()

    def cusine_type(self):
        return self.cuisine_type()

    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")


r = Restaurant("Kotipizza", "pizza")
print(r.name)
print(r.cusine_type)
r.describe_restaurant()
r.open_restaurant()
