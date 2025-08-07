class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0   # Private attribute using double underscore

    # Public method to start the car
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started.")

    # Getter method (to read speed safely)
    def get_speed(self):
        return self.__speed

    # Setter method (to update speed with rules)
    def accelerate(self, increment):
        if increment < 0:
            print("Bro you can't increase speed with a negative value.")
            return
        self.__speed += increment
        print(f"Accelerated! New speed: {self.__speed} km/h")

    # Another method to stop the car
    def stop(self):
        self.__speed = 0
        print(f"{self.brand} {self.model} stopped.")

# Creating a car object
my_car = Car("Hyundai", "i20")

# Start the car
my_car.start_engine()

# Try to access private attribute directly (not recommended)
# print(my_car.__speed)  # Will raise an error: AttributeError

# Proper way: use getter
print("Current Speed:", my_car.get_speed())

# Accelerate the car
my_car.accelerate(30)
print("Speed now:", my_car.get_speed())

# Try to accelerate with negative value (should be blocked)
my_car.accelerate(-10)

# Stop the car
my_car.stop()
print("Speed after stop:", my_car.get_speed())

# Bypass warning (just for learning, not recommended)
# You *can* access __speed like this:
print("Hacked Speed Access:", my_car._Car__speed)  # Not advised

"""
__speed:
This line creates a private attribute called __speed. 
In many OOP languages like Java or C++, when you say private, it means:
“You can’t access this variable outside the class. Period.”

But in Python, nothing is truly private. It follows a concept called:
Name Mangling

When you write __speed, Python renames it internally to: _Car__speed
That’s why this works: print(my_car._Car__speed)
So it's not magic — just a trick to make it a bit harder to access.

"""