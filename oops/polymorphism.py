# Parent class
class Car:
    def start_engine(self):
        print("Car engine started. Basic vroom.")

# Child class: SportsCar overrides the method
class SportsCar(Car):
    def start_engine(self):
        print("SportsCar engine started. Turbo VROOOOOM!")

# Child class: Truck also overrides the method
class Truck(Car):
    def start_engine(self):
        print("Truck engine started. Heavy GRRRRRRR!")

# One more class: ElectricCar, not even inheriting, but has the same method
class ElectricCar:
    def start_engine(self):
        print("ElectricCar started silently...")

# Function that shows polymorphism
def start_any_car(car_object):
    # Polymorphism: this works as long as object has start_engine()
    car_object.start_engine()

# Creating objects
basic_car = Car()
lambo = SportsCar()
tata_truck = Truck()
tesla = ElectricCar()

# Using polymorphism
start_any_car(basic_car)     # Car engine started. Basic vroom.
start_any_car(lambo)         # SportsCar engine started. Turbo VROOOOOM!
start_any_car(tata_truck)    # Truck engine started. Heavy GRRRRRRR!
start_any_car(tesla)         # ElectricCar started silently... 

"""
Same method name → .start_engine()
Different behavior based on object type → Car, SportsCar, Truck, ElectricCar
Same function call behaves differently based on the object passed
"""