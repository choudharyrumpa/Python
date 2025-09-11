# Example program to understand Python classes

# Defining a class "Car"
class Car:
    # Constructor method (__init__) is called when we create an object
    def __init__(self, brand, model, year):
        # Attributes (variables) of the class
        self.brand = brand
        self.model = model
        self.year = year
        self.is_started = False  # Default value

    # Method to start the car
    def start(self):
        if not self.is_started:
            self.is_started = True
            print(f"{self.brand} {self.model} started!")
        else:
            print(f"{self.brand} {self.model} is already running.")

    # Method to stop the car
    def stop(self):
        if self.is_started:
            self.is_started = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print(f"{self.brand} {self.model} is already stopped.")

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")


# -------------------------
# Creating objects (instances) of Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing class methods
car1.display_info()   # Prints details of car1
car1.start()          # Starts car1
car1.start()          # Trying to start again
car1.stop()           # Stops car1

print()  # Blank line for clarity

car2.display_info()   # Prints details of car2
car2.start()          # Starts car2
car2.stop()           # Stops car2
