# Assignment 1: Design Your Own Class! 🏗️
class Phone:
    # Constructor method to initialize the attributes of the class
    # This method is called when an object of the class is created
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
phoneDetails = Phone("Samsung Galaxy S22 Ultra", "Samsung", 60000)

print(phoneDetails.name)
print(phoneDetails.brand)
print(phoneDetails.price)