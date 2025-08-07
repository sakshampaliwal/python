# Base/Parent class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        print(f"{self.year} {self.brand} {self.model}")

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started... Vroooom!")

# Child class 1: SportsCar inherits from Car
class SportsCar(Car):
    def __init__(self, brand, model, year, top_speed):
        # Call the parent class constructor using super()
        super().__init__(brand, model, year)
        self.top_speed = top_speed

    def describe(self):
        # Overriding parent method
        print(f"{self.year} {self.brand} {self.model} (Sports Car) - Top speed: {self.top_speed} km/h")

    def launch_control(self):
        print(f"{self.brand} {self.model} launched with max acceleration!")

# Child class 2: Truck inherits from Car
class Truck(Car):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

    def describe(self):
        print(f"{self.year} {self.brand} {self.model} (Truck) - Load capacity: {self.capacity} tons")

    def load_cargo(self):
        print(f"Cargo loaded in {self.brand} {self.model}")

# Creating objects
normal_car = Car("Maruti", "Baleno", 2022)
sports_car = SportsCar("Lamborghini", "Huracan", 2023, 325)
truck = Truck("Tata", "Ultra", 2021, 10)

# Using parent class methods
normal_car.describe()
normal_car.start_engine()
print()

# Using child class methods
sports_car.describe()      # Uses overridden describe()
sports_car.start_engine()  # Inherited from Car
sports_car.launch_control()# New method in SportsCar
print()

truck.describe()
truck.start_engine()
truck.load_cargo()
