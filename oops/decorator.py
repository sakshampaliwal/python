class Car:
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self._max_speed = max_speed  # "protected" variable

    @property
    def max_speed(self):
        print("Getting max speed...")
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value):
        print("Setting max speed...")
        if value < 0:
            print("Speed can't be negative!")
        else:
            self._max_speed = value

    @max_speed.deleter
    def max_speed(self):
        print("Deleting max speed...")
        del self._max_speed

# Create a Car object
car = Car("BMW", "M4", 250)

# Access like a variable (but calls the getter)
print(car.max_speed)     # Output: Getting max speed... 250

# Set like a variable (but calls the setter)
car.max_speed = 300      # Output: Setting max speed...

# Try setting a negative value
car.max_speed = -50      # Output: Speed can't be negative!

# Delete like a variable (but calls deleter)
del car.max_speed        # Output: Deleting max speed...

"""
Decorators:
decorator is like a filter or wrapper that you put on top of a function/method to change or enhance how it behaves — without changing its actual code.

what is @property?
This is a built-in decorator that turns a method into a property.
So instead of calling it like a method car.get_speed(),
you can just do car.speed — like you’re accessing a variable, but it’s actually calling a function behind the scenes.
It Makes a method accessible like an attribute



"""