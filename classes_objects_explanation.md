# Python Classes and Objects

## What is a Class?

A class in Python is like a blueprint or template that defines the structure and behavior for creating objects.

```python
class Vehicle:
    """
    A simple class representing a vehicle.
    """
    def __init__(self, make, model, color, year):
        # Initialize instance attributes
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.is_running = False
```

## What is an Object?

An object is a specific instance created from a class. It contains real data and can perform actions defined by its class.

```python
# Creating objects (instances) of the Vehicle class
car1 = Vehicle("Toyota", "Corolla", "blue", 2020)
car2 = Vehicle("Tesla", "Model 3", "red", 2023)
car3 = Vehicle("Honda", "Civic", "silver", 2019)
```

## Key Concepts

### 1. Attributes

Attributes are variables that store data within a class or object.

- **Instance attributes**: Belong to a specific object instance (defined with `self.attribute_name`)
- **Class attributes**: Shared by all instances of a class (defined directly in the class)

```python
# Accessing an attribute
print(car1.color)  # Output: blue

# Modifying an attribute
car3.color = "black"
```

### 2. Methods

Methods are functions defined within a class that describe the behaviors of the objects.

```python
def start_engine(self):
    """Start the vehicle's engine"""
    if not self.is_running:
        self.is_running = True
        return f"The {self.color} {self.make} {self.model}'s engine starts. Vroom!"
    else:
        return f"The {self.make} {self.model}'s engine is already running."
```

### 3. Self Parameter

The `self` parameter refers to the specific instance of the class that is being operated on.

```python
# When we call:
car1.start_engine()

# Python interprets this as:
Vehicle.start_engine(car1)
```

### 4. Constructor Method

The `__init__` method initializes a new object with specified attributes when it's created.

```python
def __init__(self, make, model, color, year):
    self.make = make
    self.model = model
    self.color = color
    self.year = year
    self.is_running = False
```

## Analogy

Think of a class as a cookie cutter, and objects as the cookies:

- The cookie cutter (class) defines the shape and structure
- Each cookie (object) has the same shape but can have different decorations (attribute values)
- You can make many different cookies from one cookie cutter

## Complete Example

```python
class Vehicle:
    """
    A simple class representing a vehicle.
    """
    def __init__(self, make, model, color, year):
        # Initialize instance attributes
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.is_running = False
    
    def start_engine(self):
        """Start the vehicle's engine"""
        if not self.is_running:
            self.is_running = True
            return f"The {self.color} {self.make} {self.model}'s engine starts. Vroom!"
        else:
            return f"The {self.make} {self.model}'s engine is already running."
    
    def stop_engine(self):
        """Stop the vehicle's engine"""
        if self.is_running:
            self.is_running = False
            return f"The {self.make} {self.model}'s engine stops."
        else:
            return f"The {self.make} {self.model}'s engine is already off."
    
    def honk(self):
        """Make the vehicle honk its horn"""
        return f"The {self.make} {self.model} goes BEEP BEEP!"
    
    def describe(self):
        """Return a description of the vehicle"""
        status = "running" if self.is_running else "not running"
        return f"This is a {self.year} {self.color} {self.make} {self.model}. The engine is {status}."


# Creating objects (instances) of the Vehicle class
car1 = Vehicle("Toyota", "Corolla", "blue", 2020)
car2 = Vehicle("Tesla", "Model 3", "red", 2023)
car3 = Vehicle("Honda", "Civic", "silver", 2019)

# Using the objects by calling their methods
print(car1.describe())
print(car1.start_engine())
print(car1.honk())

print("\n" + car2.describe())
print(car2.start_engine())
print(car2.stop_engine())

print("\n" + car3.describe())
print(car3.honk())

# Accessing and modifying object attributes
print(f"\nBefore modification: {car3.color}")
car3.color = "black"  # Changing an attribute
print(f"After modification: {car3.color}")
print(car3.describe())  # Notice the color change in the description
```

## Why Use Classes and Objects?

1. **Organization**: Group related data and functions together
2. **Reusability**: Create multiple objects from the same blueprint
3. **Encapsulation**: Bundle data and methods that work on that data
4. **Abstraction**: Hide complex implementation details
5. **Inheritance**: Build new classes based on existing ones