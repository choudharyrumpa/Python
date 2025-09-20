# Example of Inheritance in Python

# Parent class (Base class)
class Animal:
    def __init__(self, name):
        self.name = name

    # Method inside parent class
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (Derived class) inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling parent class constructor using super()
        super().__init__(name)
        self.breed = breed

    # Overriding parent method
    def speak(self):
        print(f"{self.name} barks. Breed: {self.breed}")

# Another Child class (Derived class)
class Cat(Animal):
    # Overriding speak method
    def speak(self):
        print(f"{self.name} meows.")

# Main Program
# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Tommy", "Golden Retriever")
cat = Cat("Kitty")

# Calling methods
animal.speak()   # Uses Animal's speak
dog.speak()      # Uses Dog's overridden speak
cat.speak()      # Uses Cat's overridden speak
