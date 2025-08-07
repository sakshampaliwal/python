class Car:
    def __init__(self, brand, model, car_type):
        self.brand = brand
        self.model = model
        self.car_type = car_type

    def describe(self):
        print(f"{self.brand} {self.model} ({self.car_type})")

    @staticmethod
    def is_electric(car_type):
        # No need to access any object data (no self)
        electric_types = ['EV', 'Electric', 'Hybrid']
        return car_type in electric_types

print(Car.is_electric("EV"))         # True
print(Car.is_electric("Petrol"))     # False

my_car = Car("Tata", "Nexon", "EV")
print(Car.is_electric(my_car.car_type))  # True


"""
We’re calling it directly from the class — like Car.is_electric(...) — because:

- It doesn’t need self
- It’s not connected to any specific car object
- It's just a general yes/no check

Even if you have an object, you still don’t need it:

    my_car = Car("Tata", "Nexon", "EV")
    print(Car.is_electric(my_car.car_type))  # Still works

We used the object to get the car type, but we still called the function using the class.
Because is_electric() doesn’t use the object at all.

Why put static methods inside a class when they don’t use self? Why not just make a regular function?

Totally valid. But now this function is floating in your file. There’s no way to tell it's related to Car unless you read the code or comment it.
It’s like saying:
 “This function doesn’t touch the Car object, but it’s still something you’d want to group with other car-related stuff.”

But with static method:

- You grouped everything about a car in the Car class
- Any dev reading your code sees that is_electric() is part of car-related logic
- It keeps your code clean and logically encapsulated

If your function is a general utility used everywhere in the app — not specific to cars — then yeah bro, make it a regular function.
"""
