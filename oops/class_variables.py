class Car:
    # CLASS VARIABLE — shared across all Car objects
    wheels = 4  # Default number of wheels for all cars
    traffic_rules = "Follow speed limits and traffic lights 🚦"

    def __init__(self, brand, model):
        # INSTANCE VARIABLES — unique to each object
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"{self.brand} {self.model} has {Car.wheels} wheels.")

    def show_rules(self):
        print(f"Traffic rules: {Car.traffic_rules}")

# Creating objects
car1 = Car("Maruti", "Swift")
car2 = Car("Hyundai", "i20")

# Accessing class variable from instances
car1.describe()     # Output: Maruti Swift has 4 wheels.
car2.describe()     # Output: Hyundai i20 has 4 wheels.

# Access class variable using class name (preferred)
print(Car.traffic_rules)     # Output: Follow speed limits...

# Access from instance (also works but not preferred)
car1.show_rules()

# Modify class variable
Car.wheels = 6   # Changing for ALL cars

print("\nAfter updating wheels...\n")
car1.describe()     # Now shows 6 wheels
car2.describe()     # Also shows 6 wheels

# But what if an object sets it on its own?
car1.wheels = 8     # This creates a new instance variable ONLY for car1

print("\nAfter car1 changes its wheels...\n")
print(f"car1 wheels: {car1.wheels}")  # 8 (instance variable now)
print(f"car2 wheels: {car2.wheels}")  # 6 (still uses class variable)
print(f"Car.wheels : {Car.wheels}")   # 6 (class variable)
