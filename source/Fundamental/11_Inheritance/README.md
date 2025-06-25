## Chapter 11: Inheritance

This chapter expands on the concept of inheritance, one of the cornerstones of Object-Oriented Programming. We'll delve
deeper into how to effectively use inheritance to create robust and extensible class hierarchies.

### 1. Basics of Inheritance

#### Understanding the Concept of Inheritance

As introduced in Chapter 10, inheritance allows a new class (subclass or child class) to derive properties and
behaviors (attributes and methods) from an existing class (superclass or parent class). This creates an "is-a"
relationship, meaning the subclass "is a" specialized type of the superclass. For example, a `Car` "is a" `Vehicle`.

Key advantages of inheritance include:

* **Code Reusability:** Avoids writing the same code multiple times.
* **Extensibility:** Easier to add new features or modify existing ones without affecting other parts of the code.
* **Maintainability:** Changes in the parent class can automatically propagate to subclasses.

#### Creating Subclasses and Using the `super()` Function

To create a subclass, you simply list the parent class in parentheses after the subclass name:

```python
class Vehicle:  # Parent class
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.make} {self.model}"


class Car(Vehicle):  # Car is a subclass of Vehicle
    def __init__(self, make, model, year):
        # Call the parent class's __init__ method using super()
        super().__init__(make, model)
        self.year = year

    def display_car_info(self):
        return f"{self.display_info()}, Year: {self.year}"


# Create instances
my_vehicle = Vehicle("Generic", "ModelX")
my_car = Car("Toyota", "Camry", 2023)

print(my_vehicle.display_info())  # Output: Vehicle: Generic ModelX
print(my_car.display_info())  # Output: Vehicle: Toyota Camry (inherited method)
print(my_car.display_car_info())  # Output: Vehicle: Toyota Camry, Year: 2023
```

The `super()` function is essential when working with inheritance. It allows you to call methods from the parent class (
superclass) within the subclass.

* **`super().__init__(...)`:** This is the most common use case. It ensures that the parent class's constructor (
  `__init__`) is called to initialize the attributes defined in the parent. This is crucial for properly setting up the
  inherited part of the object.
* `super().method_name(...)`: Can be used to call other methods of the parent class, not just the constructor.

### 2. Method Overriding

#### Overriding Methods in the Subclass

Method overriding occurs when a subclass provides its own implementation of a method that is already defined in its
parent class. When an instance of the subclass calls that method, the subclass's version is executed instead of the
parent's. This is a key aspect of polymorphism.

```python
class Bird:
    def speak(self):
        return "Chirp!"


class Parrot(Bird):
    def speak(self):  # Overriding the speak method
        return "Squawk! I can talk!"


class Penguin(Bird):
    def speak(self, action="waddle"):  # Overriding with a different signature (though not good practice)
        return f"Penguin goes {action}."


bird = Bird()
parrot = Parrot()
penguin = Penguin()

print(bird.speak())  # Output: Chirp!
print(parrot.speak())  # Output: Squawk! I can talk!
print(penguin.speak())  # Output: Penguin goes waddle.
```

While Python allows different method signatures when overriding (like `penguin.speak()` vs `bird.speak()`), it's
generally considered good practice to maintain consistent signatures for clarity and to fully leverage polymorphism.

#### Using Polymorphism with Inheritance

As seen in Chapter 10, polymorphism allows objects of different classes (that share a common parent) to be treated
through a common interface.

```python
def make_it_speak(creature):
    print(creature.speak())


make_it_speak(bird)
make_it_speak(parrot)
make_it_speak(penguin)  # This will work, but consider the signature mismatch
```

This demonstrates how the `make_it_speak` function can operate on any `Bird` object or its subclasses, relying on each
object's specific `speak` implementation.

### 3. Inheritance and Class Hierarchies

#### Designing Class Hierarchies

A class hierarchy is a tree-like structure where classes inherit from other classes, forming a logical organization.
Designing effective class hierarchies is crucial for building scalable and maintainable object-oriented applications.

**Guidelines for good hierarchy design:**

* **"Is-a" Relationship:** Ensure that the subclass genuinely "is a" type of the superclass.
* **Commonality:** Group common attributes and behaviors into higher-level parent classes.
* **Specialization:** Subclasses should represent more specialized versions of the parent.
* **Depth:** Avoid excessively deep hierarchies, as they can become complex to manage.
* **Single Responsibility Principle:** Each class should have a single, well-defined responsibility.

**Example of a simple hierarchy:**

```
Shape (abstract concept)
├── Circle
├── Rectangle
└── Triangle

Vehicle (abstract concept)
├── Car
├── Motorcycle
└── Bicycle
```

#### The Role of Abstract Classes and Methods

In Python, an **abstract class** is a class that cannot be instantiated directly. It serves as a blueprint for other
classes and often contains **abstract methods**, which are methods declared in the abstract class but have no
implementation. Subclasses *must* provide implementations for these abstract methods.

Python provides the `abc` (Abstract Base Classes) module to create abstract classes.

```python
from abc import ABC, abstractmethod


class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass  # No implementation here

    @abstractmethod
    def perimeter(self):
        pass  # No implementation here


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Must implement abstract method
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):  # Must implement abstract method
        import math
        return 2 * math.pi * self.radius


# shape = Shape() # This would raise a TypeError because Shape is abstract

my_circle = Circle(7)
print(f"Circle Area: {my_circle.area():.2f}")
print(f"Circle Perimeter: {my_circle.perimeter():.2f}")
```

Abstract classes enforce a contract: any concrete subclass must implement all abstract methods. This ensures that all
objects of that hierarchy will have a consistent interface for certain functionalities, even if their specific
implementations differ. This is extremely useful for designing frameworks and ensuring consistency in large codebases.

---
