# part 1 Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        # Call parent constructor
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
        self.battery = 100  # default full battery
    
    # Method to simulate making a call
    def make_call(self, contact):
        return f"Calling {contact} from {self.device_info()}..."
    
    # Method to simulate charging
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"Battery charged to {self.battery}%"
    
    # Override (polymorphism)
    def device_info(self):
        return f"{self.brand} {self.model} | OS: {self.os}, Storage: {self.storage}GB"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S25", "Android", 124)
phone2 = Smartphone("Apple", "iPhone 16", "iOS", 256)

print(phone1.device_info())
print(phone1.make_call("Alice"))
print(phone1.charge(20))

print(phone2.device_info())
print(phone2.make_call("Bob"))

# Part 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
