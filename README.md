**# 🚗 Python OOP Demo – Devices & Vehicles

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python, including **inheritance, encapsulation, and polymorphism**.  
It consists of two main parts:

---

## 🔹 Part 1: Device & Smartphone Classes

We create a base `Device` class and a child `Smartphone` class that inherits from it.

### Features:
- **Device (Base Class)**  
  - Attributes: `brand`, `model`  
  - Method: `device_info()` → Returns basic device info  

- **Smartphone (Child Class)**  
  - Inherits from `Device`  
  - Adds attributes: `os`, `storage`, `battery`  
  - Methods:  
    - `make_call(contact)` → Simulates calling a contact  
    - `charge(amount)` → Increases battery level (max 100%)  
    - Overrides `device_info()` → Shows full details (brand, model, OS, storage)  

### Example Usage:
```python**
**phone1 = Smartphone("Samsung", "Galaxy S25", "Android", 124)
phone2 = Smartphone("Apple", "iPhone 16", "iOS", 256)

print(phone1.device_info())    # Samsung Galaxy S25 | OS: Android, Storage: 124GB
print(phone1.make_call("Alice"))  # Calling Alice from Samsung Galaxy S25...
print(phone1.charge(20))          # Battery charged to 100%

print(phone2.device_info())    # Apple iPhone 16 | OS: iOS, Storage: 256GB
print(phone2.make_call("Bob")) # Calling Bob from Apple iPhone 16...
🔹 Part 2: Vehicle Classes

We define a base class Vehicle with a polymorphic method move(), then create multiple subclasses.

Features:

Vehicle (Base Class)

Abstract method: move() (must be implemented by subclasses)

Car, Plane, Boat (Child Classes)

Each implements move() differently:

Car → "Driving 🚗"

Plane → "Flying ✈️"

Boat → "Sailing 🚤"

Example Usage:
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

Output:
Driving 🚗
Flying ✈️
Sailing 🚤

🎯 Concepts Demonstrated

Inheritance → Smartphone inherits from Device, Car/Plane/Boat inherit from Vehicle

Polymorphism → Different implementations of device_info() and move()

Encapsulation → Controlled battery charging in Smartphone

▶️ Running the Code

Run the script with Python 3:

python main.py


(Replace main.py with your filename)

📚 Learning Goal

This project is designed to help beginners understand how classes, constructors, methods, inheritance, and polymorphism work in Python.
