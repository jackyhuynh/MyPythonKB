## Chapter 10: Classes and Object-Oriented Programming

This chapter marks a significant shift in how we structure our code, moving from procedural programming to *
*Object-Oriented Programming (OOP)**. OOP is a powerful paradigm that allows us to model real-world entities and their
interactions, leading to more organized, maintainable, and reusable code.

### 1. Introduction to Object-Oriented Programming (OOP)

#### Understanding the Basics of OOP

OOP is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods).
The core idea is to bundle data and the functions that operate on that data into a single unit. This approach helps
manage complexity in large applications by creating modular, self-contained units.

#### Concepts of Classes, Objects, Attributes, and Methods

* **Class:** A blueprint or a template for creating objects. It defines the common attributes and methods that all
  objects of that class will have. Think of a class as the design for a car – it specifies what a car has (wheels,
  engine, color) and what it can do (drive, stop, accelerate).

* **Object (Instance):** An individual instance of a class. When you create an object from a class, you are creating a
  concrete realization of that blueprint. Using the car analogy, an object is a specific car built according to the
  design – say, a blue Ford Mustang.

* **Attribute:** A variable associated with a class or an object. Attributes represent the characteristics or properties
  of an object. For a `Car` object, attributes might include `color`, `make`, `model`, and `speed`.

* **Method:** A function defined inside a class that operates on the object's data (attributes). Methods define the
  behaviors or actions that an object can perform. For a `Car` object, methods might include `start_engine()`,
  `accelerate()`, `brake()`, and `turn()`.

### 2. Defining Classes

#### Creating and Using Classes

In Python, you define a class using the `class` keyword, followed by the class name (conventionally capitalized using
`CamelCase`).

```python
class Dog:
    # Class attributes (shared by all instances)
    species = "Canis familiaris"

    # The __init__ method is a special method called a constructor
    def __init__(self, name, breed):
        # Instance attributes (unique to each instance)
        self.name = name
        self.breed = breed
        self.is_sitting = False # Default state

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    def sit(self):
        if not self.is_sitting:
            self.is_sitting = True
            return f"{self.name} is now sitting."
        else:
            return f"{self.name} is already sitting."

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")

# Accessing attributes
print(dog1.name)    # Output: Buddy
print(dog2.breed)   # Output: Labrador
print(dog1.species) # Output: Canis familiaris (accessing class attribute)

# Calling methods
print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.sit())   # Output: Lucy is now sitting.
print(dog2.sit())   # Output: Lucy is already sitting.
```

#### The `__init__` Method and Instance Attributes

The `__init__` method is a special method in Python classes. It's called automatically when a new object (instance) of
the class is created. Its primary purpose is to initialize the object's attributes.

* `self`: The first parameter of any instance method (including `__init__`) is always `self`. It's a conventional name
  that refers to the instance of the class being created or operated on. When you call `dog1.bark()`, `self` inside
  `bark()` refers to `dog1`.
* **Instance Attributes:** Attributes defined within the `__init__` method (e.g., `self.name = name`) are called
  instance attributes. Each object will have its own unique set of these attributes, storing specific data for that
  instance.

### 3. Methods

#### Defining and Using Instance Methods

Instance methods are functions defined within a class that operate on the instance's attributes. They always take `self`
as their first parameter, allowing them to access and modify the object's state.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        import math
        return math.pi * (self.radius ** 2)

    def calculate_circumference(self):
        import math
        return 2 * math.pi * self.radius

# Create an instance
my_circle = Circle(5)

# Call instance methods
print(f"Area: {my_circle.calculate_area():.2f}")
print(f"Circumference: {my_circle.calculate_circumference():.2f}")
```

#### Understanding `self` and its Role in Class Methods

As mentioned, `self` is a reference to the instance itself. It's crucial because it allows methods to:

1. **Access Instance Attributes:** `self.radius` allows `calculate_area` to know which circle's radius it should use.
2. **Modify Instance Attributes:** If a method needs to change the state of the object, it does so by modifying `self`'s
   attributes (e.g., `self.is_sitting = True`).
3. **Call Other Instance Methods:** An instance method can call another instance method using `self.another_method()`.

While `self` is the convention, you *could* use another name, but it's strongly discouraged for readability and
adherence to Python community standards.

### 4. Inheritance

Inheritance is a fundamental OOP principle that allows a new class (subclass or child class) to inherit attributes and
methods from an existing class (superclass or parent class). This promotes code reusability and establishes a natural "
is-a" relationship between classes (e.g., a "Dog is a Mammal").

#### Implementing Inheritance in Python

To inherit from a class, you specify the parent class in parentheses after the subclass name.

```python
class Animal: # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

class Dog(Animal): # Dog is a subclass of Animal
    def __init__(self, name, breed):
        super().__init__(name) # Call the parent class's __init__ method
        self.breed = breed

    def speak(self): # Overriding the speak method
        return f"{self.name} barks!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}."

class Cat(Animal): # Cat is also a subclass of Animal
    def speak(self): # Overriding the speak method
        return f"{self.name} meows!"

# Create instances
animal = Animal("Creature")
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers")

print(animal.speak()) # Output: Generic animal sound
print(dog.speak())    # Output: Rex barks!
print(cat.speak())    # Output: Whiskers meows!
print(dog.fetch("ball")) # Output: Rex fetches the ball.
```

#### Understanding the Benefits of Inheritance

* **Code Reusability:** Avoids duplicating code. Common attributes and methods are defined once in the parent class and
  inherited by all subclasses.
* **Modularity:** Promotes a cleaner, more organized structure by grouping related functionalities.
* **Extensibility:** Easier to extend existing functionality by creating new subclasses without modifying the original
  code.
* **Polymorphism (covered next):** Enables objects of different classes to be treated uniformly.

### 5. Polymorphism

Polymorphism (meaning "many forms") is the ability of objects of different classes to respond to the same method call in
their own specific way. It allows you to write more generic and flexible code.

#### Understanding Polymorphism and Method Overriding

* **Method Overriding:** A subclass can provide its own implementation of a method that is already defined in its
  superclass. When this happens, the subclass's version of the method is called instead of the superclass's version.
  This is what we saw with the `speak()` method in the `Dog` and `Cat` classes.

* **Polymorphism in Action:**
  Consider a function that takes an `Animal` object and calls its `speak()` method:

    ```python
    def make_animal_speak(animal):
        print(animal.speak())

    make_animal_speak(animal) # Output: Generic animal sound
    make_animal_speak(dog)    # Output: Rex barks!
    make_animal_speak(cat)    # Output: Whiskers meows!
    ```
  Even though `make_animal_speak` always calls `animal.speak()`, the actual behavior changes depending on the *type* of
  object passed to it. This is polymorphism – the same method call (`speak()`) takes different forms depending on the
  object it's invoked on.

Polymorphism greatly simplifies code and makes it more adaptable to future changes, as you can work with a common
interface without needing to know the specific type of object at compile time.

---