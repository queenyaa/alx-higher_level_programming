Readme of 0x06-python-classes

# Object-Oriented Programming in Python

This repository contains Python code that demonstrates object-oriented programming (OOP) concepts using classes and objects. Each task represents a different aspect of OOP and covers a variety of topics, including class attributes, instance attributes, methods, properties, and more. The tasks are designed to showcase best practices in Python OOP and include proper documentation.

## Task 0: Empty Class Square

**File**: `0-square.py`

- Description: This task introduces the concept of defining a class with minimal functionality.
- Objective: Create an empty `Square` class with no attributes or methods.

## Task 1: Square with Size

**File**: `1-square.py`

- Description: This task adds a private instance attribute and an initialization method to the `Square` class.
- Objective: Create a `Square` class with a private attribute `size` and an `__init__` method to initialize it.

## Task 2: Validate Size Value

**File**: `2-square.py`

- Description: This task adds validation for the `size` attribute, raising exceptions for invalid input.
- Objective: Add checks to ensure that `size` is an integer and greater than or equal to 0.

## Task 3: Calculate Square Area

**File**: `3-square.py`

- Description: This task introduces a public instance method to calculate the area of the square.
- Objective: Add an `area` method to compute and return the area of the square.

## Task 4: Setter and Getter for Size

**File**: `4-square.py`

- Description: This task implements property getters and setters for the `size` attribute.
- Objective: Create properties for `size` to allow getting and setting its value with validation.

## Task 5: Print a Square

**File**: `5-square.py`

- Description: This task adds a public instance method to print the square with `#` characters.
- Objective: Implement a `my_print` method to display the square, considering its size.

## Task 6: Positional Printing

**File**: `6-square.py`

- Description: This task adds a private instance attribute `position` and properties for it.
- Objective: Introduce `position` to control the printing position of the square, and update `my_print` accordingly.

## Task 7: Singly Linked List

**File**: `100-singly_linked_list.py`

- Description: This task defines a singly linked list using classes.
- Objective: Create classes for `Node` and `SinglyLinkedList`, allowing operations like adding nodes and printing the list.

## Task 8: Compare Squares

**File**: `101-square.py`

- Description: This task enables comparison of `Square` instances based on their areas.
- Objective: Implement comparison methods (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`) for squares.

## Task 9: MagicClass

**File**: `102-magic_calculation.py`

- Description: This task requires implementing a class that performs mathematical calculations similar to provided bytecode.
- Objective: Create a `MagicClass` class with methods for area and circumference calculations.

## Usage

To use any of the classes defined in the tasks, you can create instances of the classes and call their methods as demonstrated in each task's file.

For example:

```python
# Creating a Square instance with size
my_square = Square(5)

# Calculating and printing the area of the square
print(f"Area: {my_square.area()}")

# Comparing two Square instances
square1 = Square(4)
square2 = Square(5)
if square1 < square2:
    print("Square 1 is smaller than Square 2")
```

Feel free to explore and modify the code to understand the concepts and practice OOP in Python. 
