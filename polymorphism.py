# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Animal:
    def move(self):
        print("Moving")

class Dog(Animal):
    def move(self):
        print("Running")

class Cat(Animal):
    def move(self):
        print("Walking")

class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")
        
# Create instances of each class
dog = Dog()
cat = Cat()
car = Car()
plane = Plane()

# Call the move method for each instance
dog.move()
cat.move()
car.move()
plane.move()
    