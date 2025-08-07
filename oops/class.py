# Defining a class - this is like a blueprint for making cars
class Car:
    # This function is called when you create a new Car (object/instance)
    def __init__(self, brand, model, car_type, year, color):
        # These are attributes(nothing but variables). Each car will have its own brand, model, etc.
        self.brand = brand
        self.model = model
        self.car_type = car_type
        self.year = year
        self.color = color

    # A method (a function inside a class) to describe the car
    def describe(self):
        print(f"{self.color} {self.year} {self.brand} {self.model} ({self.car_type})")

    # Another method to simulate starting the car
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started... Vroooom!")

# Creating objects (also called instances) of the Car class

# This is object 1
my_car = Car("Toyota", "Fortuner", "SUV", 2022, "Black")

# This is object 2
your_car = Car("Tata", "Punch", "Hatchback", 2023, "Red")

# Accessing attributes
print(my_car.brand)         # Output: Toyota
print(your_car.model)       # Output: Punch

# Using methods
my_car.describe()           # Output: Black 2022 Toyota Fortuner (SUV)
your_car.describe()         # Output: Red 2023 Tata Punch (Hatchback)

# Starting engine
my_car.start_engine()       # Output: Toyota Fortuner's engine started... Vroooom!
your_car.start_engine()     # Output: Tata Punch's engine started... Vroooom!


"""""
-------------------------------------------------------------------------------
self:
- 'self' is a way to access the variables and methods that belong to the class instance.
- Behind the scenes:
    1. Python creates an empty object (e.g., my_car)
    2. It calls the __init__() method
    3. It passes 'self' as a reference to this specific object you're creating
    4. It stores the data in attributes like self.brand, self.model, etc.
- So 'self' is basically that individual object (like my_car) that you're building.

__init__()
- This is a constructor method in Python.
- Any method that starts and ends with double underscores (like __init__, __str__, __len__, etc.)
    is a "special method" or "dunder method" (short for Double UNDERscore).
- __init__() gets called automatically when you create a new object from a class.

Example:
- If you run this code: my_car = Car("Toyota", "Fortuner", "SUV", 2022, "Black")
- Python does this behind the scenes:
    new_car = Car.__init__(new_car, "Toyota", "Fortuner", "SUV", 2022, "Black")

try this code:
class Car:
    def __init__(self, brand):
        print("Self is:", self)  # will print memory address of the object
        self.brand = brand

my_car = Car("Hyundai")
print("My car brand:", my_car.brand)

"""""