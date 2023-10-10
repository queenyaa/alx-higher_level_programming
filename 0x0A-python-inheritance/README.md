Readme of 0x0A-python-inheritance

##Task 0 Documentation: Object Attributes and Methods Lookup##

**Description:**

The task involves creating a Python function called `lookup` that returns a list of available attributes and methods of an object. This function is designed to help users inspect and understand the content and capabilities of an object.

**Function Prototype:**

```python
def lookup(obj):
    """
    Returns a list object containing the names of attributes and methods of the given object.

    :param obj: The object to inspect.
    :return: A list of attribute and method names.
    """
```

**Parameters:**

- `obj` (object): The input object for which you want to retrieve attribute and method names.

**Return Value:**

- A list containing the names of attributes and methods of the input object.

**Usage:**

You can use this function to examine the available attributes and methods of any object. Here's how you can use it:

```python
# Import the lookup function
lookup = __import__('0-lookup').lookup

# Example usage with MyClass
class MyClass(object):
    def __init__(self):
        self.my_attribute = 42

    def my_method(self):
        return "Hello, World!"

obj = MyClass()

# Get the list of attributes and methods
attributes_and_methods = lookup(obj)

# Print the result
print(attributes_and_methods)
```

**Output:**

```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attribute', 'my_method']
```

This documentation provides an overview of the `lookup` function, its purpose, usage, and expected output. It allows you to introspect objects and understand their structure more effectively.


##Task 1: Creating a MyList Class##

```
Task 1: Creating a MyList Class

Description:
-------------------------
Task 1 involves creating a Python class named MyList that inherits from the built-in list class. This class adds a custom method called print_sorted to the list, which prints the elements of the list in ascending order.

Class Details:
-------------------------
Class Name: MyList
Base Class: list (inherits from the built-in list class)

Methods:
-------------------------
1. def print_sorted(self):
    - Description: This method prints the elements of the list in ascending order.
    - Parameters: None (other than self, which refers to the instance of the MyList class).
    - Return Value: None
    - Assumptions: It is assumed that all elements in the list will be of type int.

Usage Example:
-------------------------
MyList is instantiated as an object, and elements are added to it using the standard list methods such as append(). The print_sorted() method is then called to display the list in sorted order.

Example Code:
-------------------------
# Instantiate MyList
my_list = MyList()

# Add elements to the list
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

# Print the original list
print(my_list)

# Print the sorted list
my_list.print_sorted()

# Print the original list again
print(my_list)

Expected Output:
-------------------------
[1, 4, 2, 3, 5]  # Original list
[1, 2, 3, 4, 5]  # Sorted list
[1, 4, 2, 3, 5]  # Original list (unchanged)

Notes:
-------------------------
- The MyList class inherits all the functionality of the list class and adds the ability to print the list in sorted order.
- This task does not allow importing external modules, and it assumes that all elements in the list are of type int.

```

##Task 2 Documentation: Object Comparison by Class##

**Description:**

Task 2 involves the implementation of a Python function called `is_same_class`. This function checks if an object is an instance of a specified class. It returns `True` if the object is exactly an instance of the specified class, and `False` otherwise.

**Function Prototype:**

```python
def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class, False otherwise.
    """
```

**Parameters:**

- `obj` (object): The object to be checked.
- `a_class` (type or class): The class to compare `obj` with.

**Return Value:**

- `True` if `obj` is an instance of `a_class`.
- `False` if `obj` is not an instance of `a_class`.

**Usage:**

You can use the `is_same_class` function to determine whether an object belongs to a specific class. Here's an example of how to use it:

```python
# Import the is_same_class function
is_same_class = __import__('2-is_same_class').is_same_class

# Example usage
a = 1

if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
else:
    print("{} is not an instance of the class {}".format(a, int.__name__))
```

**Output:**

```
1 is an instance of the class int
```

##Task 3 Documentation: Object Type Checking##

**Description:**

Task 3 involves the implementation of a Python function called `is_kind_of_class`. This function checks if an object is an instance of a specified class or any class that inherits from it. It returns `True` if the object is an instance of the specified class or its subclasses, and `False` otherwise.

**Function Prototype:**

```python
def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherits from, the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class or its subclass, False otherwise.
    """
```

**Parameters:**

- `obj` (object): The object to be checked.
- `a_class` (type or class): The class to compare `obj` with.

**Return Value:**

- `True` if `obj` is an instance of `a_class` or one of its subclasses.
- `False` if `obj` is not an instance of `a_class` or its subclasses.

**Usage:**

You can use the `is_kind_of_class` function to determine whether an object belongs to a specific class or its subclasses. Here's an example of how to use it:

```python
# Import the is_kind_of_class function
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

# Example usage
a = 1

if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
else:
    print("{} doesn't come from {}".format(a, int.__name__))
```

**Output:**

```
1 comes from int
```


##Task 4 Documentation: Inheritance Checker##

**Description:**

Task 4 involves the implementation of a Python function called `inherits_from`. This function checks if an object is an instance of a class that directly or indirectly inherits from a specified class. It returns `True` if the object is an instance of a class that inherits from the specified class, and `False` otherwise.

**Function Prototype:**

```python
def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherits (directly or indirectly) from a specified class.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a subclass of a_class, False otherwise.
    """
```

**Parameters:**

- `obj` (object): The object to be checked.
- `a_class` (type or class): The class to compare `obj` with.

**Return Value:**

- `True` if `obj` is an instance of a class that inherits (directly or indirectly) from `a_class`.
- `False` if `obj` is not an instance of such a class.

**Usage:**

You can use the `inherits_from` function to determine whether an object is an instance of a class that inherits from a specific class or any of its subclasses. Here's an example of how to use it:

```python
# Import the inherits_from function
inherits_from = __import__('4-inherits_from').inherits_from

# Example usage
a = True

if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
else:
    print("{} didn't inherit from class {}".format(a, int.__name__))
```

**Output:**

```
True inherited from class int
```

##Task 5 Documentation: BaseGeometry Class##

**Description:**

Task 5 involves the creation of a Python class called `BaseGeometry`. This class serves as a base class for geometric objects and defines some fundamental properties and methods related to geometry.

**Class Definition:**

```python
class BaseGeometry:
    """
    A base class for geometric objects.

    This class provides a foundation for geometric objects and defines basic properties and methods related to geometry.

    Attributes:
        None

    Methods:
        area(): Placeholder method for calculating the area of geometric objects.
    """
```

**Attributes:**

- This class does not have any specific attributes.

**Methods:**

- `area(self)`: This is a placeholder method for calculating the area of geometric objects. It raises an `Exception` with the message "area() is not implemented" when called. Subclasses of `BaseGeometry` should implement this method to calculate the area of specific geometric shapes.

**Usage:**

You can use the `BaseGeometry` class as a base class for creating more specialized geometric classes. Here's an example of how to use it:

```python
# Import the BaseGeometry class
BaseGeometry = __import__('5-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

# Attempt to calculate the area (placeholder method)
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

**Output:**

```
[Exception] area() is not implemented
```

##Task 4 Documentation: Inherits From Class Checker##

**Description:**

Task 4 involves the creation of a Python function, `inherits_from(obj, a_class)`, which checks if an object is an instance of a class that inherited (directly or indirectly) from a specified class.

**Function Definition:**

```python
def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited from a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to be checked against.

    Returns:
        True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
```

**Arguments:**

- `obj`: The object to be checked.
- `a_class`: The class to be checked against.

**Returns:**

- `True` if `obj` is an instance of a class that inherited from `a_class`.
- `False` otherwise.

**Usage:**

You can use the `inherits_from` function to determine if an object is an instance of a class that inherited (directly or indirectly) from a specified class. Here's an example of how to use it:

```python
# Import the inherits_from function
inherits_from = __import__('4-inherits_from').inherits_from

# Create an object and check if it inherits from int
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))

# Create an object and check if it inherits from bool
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))

# Create an object and check if it inherits from object
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
```

**Output:**

```
True inherited from class int
True inherited from class object
```

##Task 5 Documentation: BaseGeometry Class##

**Description:**

Task 5 involves the creation of a Python class named `BaseGeometry`. This class serves as a base class and contains a basic structure for geometry-related operations.

**Class Definition:**

```python
class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class provides a basic structure for geometry operations.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented."
    """
```

**Attributes:**

- No attributes are defined in the `BaseGeometry` class.

**Methods:**

1. `area(self)`: This method raises an Exception with the message "area() is not implemented." It is intended to be overridden by subclasses to calculate the area of specific geometric shapes.

**Usage:**

You can use the `BaseGeometry` class as a base class for creating more specialized geometry-related classes. The primary purpose of this class is to provide a structure for common methods like `area`, which can be implemented in derived classes.

**Example:**

```python
# Import the BaseGeometry class
BaseGeometry = __import__('5-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

**Output:**

```
[Exception] area() is not implemented
```


##Task 6 Documentation: BaseGeometry Class with Exception

**Description:**

Task 6 builds upon Task 5 and involves extending the `BaseGeometry` class by adding an `area` method that raises an exception with a specific message. This class continues to serve as a base class for geometry-related operations.

**Class Definition:**

```python
class BaseGeometry:
    """
    A base class for geometry-related operations with an area method.

    This class provides a basic structure for geometry operations with an area method
    that raises an Exception with the message "area() is not implemented."

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented."
    """
```

**Attributes:**

- No attributes are defined in the `BaseGeometry` class.

**Methods:**

1. `area(self)`: This method raises an Exception with the message "area() is not implemented." It is intended to be overridden by subclasses to calculate the area of specific geometric shapes.

**Usage:**

You can use the `BaseGeometry` class as a base class for creating more specialized geometry-related classes. The primary purpose of this class is to provide a structure for common methods like `area`, which can be implemented in derived classes.

**Example:**

```python
# Import the BaseGeometry class
BaseGeometry = __import__('6-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

**Output:**

```
[Exception] area() is not implemented
```


##Task 6 Documentation: BaseGeometry Class with Exception

**Description:**

Task 6 builds upon Task 5 and involves extending the `BaseGeometry` class by adding an `area` method that raises an exception with a specific message. This class continues to serve as a base class for geometry-related operations.

**Class Definition:**

```python
class BaseGeometry:
    """
    A base class for geometry-related operations with an area method.

    This class provides a basic structure for geometry operations with an area method
    that raises an Exception with the message "area() is not implemented."

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented."
    """
```

**Attributes:**

- No attributes are defined in the `BaseGeometry` class.

**Methods:**

1. `area(self)`: This method raises an Exception with the message "area() is not implemented." It is intended to be overridden by subclasses to calculate the area of specific geometric shapes.

**Usage:**

You can use the `BaseGeometry` class as a base class for creating more specialized geometry-related classes. The primary purpose of this class is to provide a structure for common methods like `area`, which can be implemented in derived classes.

**Example:**

```python
# Import the BaseGeometry class
BaseGeometry = __import__('6-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

**Output:**

```
[Exception] area() is not implemented
```


##Task 7 Documentation: BaseGeometry Class with Validation

**Description:**

Task 7 extends the `BaseGeometry` class introduced in Task 6, adding a new method called `integer_validator`. This method is responsible for validating whether a given value is an integer and whether it meets certain criteria.

**Class Definition:**

```python
class BaseGeometry:
    """
    A base class for geometry-related operations with validation.

    This class provides a basic structure for geometry operations and includes
    a method for integer validation.

    Methods:
        integer_validator(self, name, value): Validates that 'value' is an integer.
    """
```

**Attributes:**

- No attributes are defined in the `BaseGeometry` class.

**Methods:**

1. `integer_validator(self, name, value)`: This method validates that the 'value' argument is an integer. If it is not, it raises a `TypeError` exception with the message "<name> must be an integer." If 'value' is an integer but is less than or equal to 0, it raises a `ValueError` exception with the message "<name> must be greater than 0."

**Usage:**

The `BaseGeometry` class serves as a base class for creating more specialized geometry-related classes that require integer validation. The `integer_validator` method can be used to ensure that specific attributes meet certain criteria.

**Example:**

```python
# Import the BaseGeometry class
BaseGeometry = __import__('7-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

# Validate an integer attribute 'my_int'
try:
    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Attempt to validate non-integer values
try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

**Output:**

```
[TypeError] my_int must be an integer
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```


##Task 7 Documentation: BaseGeometry Class with Validation

**Description:**

Task 7 extends the `BaseGeometry` class introduced in Task 6, adding a new method called `integer_validator`. This method is responsible for validating whether a given value is an integer and whether it meets certain criteria.

**Class Definition:**

```python
class BaseGeometry:
    """
    A base class for geometry-related operations with validation.

    This class provides a basic structure for geometry operations and includes
    a method for integer validation.

    Methods:
        integer_validator(self, name, value): Validates that 'value' is an integer.
    """
```

**Attributes:**

- No attributes are defined in the `BaseGeometry` class.

**Methods:**

1. `integer_validator(self, name, value)`: This method validates that the 'value' argument is an integer. If it is not, it raises a `TypeError` exception with the message "<name> must be an integer." If 'value' is an integer but is less than or equal to 0, it raises a `ValueError` exception with the message "<name> must be greater than 0."

**Usage:**

The `BaseGeometry` class serves as a base class for creating more specialized geometry-related classes that require integer validation. The `integer_validator` method can be used to ensure that specific attributes meet certain criteria.

**Example:**

```python
# Import the BaseGeometry class
BaseGeometry = __import__('7-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
basg = BaseGeometry()

# Validate an integer attribute 'my_int'
try:
    basg.integer_validator("my_int", 12)
    basg.integer_validator("width", 89)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Attempt to validate non-integer values
try:
    basg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    basg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    basg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

**Output:**

```
[TypeError] my_int must be an integer
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```


##Task 9 Documentation: Rectangle Class with Area Calculation

**Description:**

Task 9 introduces the `Rectangle` class, which inherits from the `BaseGeometry` class introduced in Task 7. The `Rectangle` class represents rectangles and includes attributes for width and height, as well as a method to calculate the area of a rectangle. Additionally, it enforces validation rules for these attributes.

**Class Definition:**

```python
class Rectangle(BaseGeometry):
    """
    A class representing a rectangle with width and height attributes.

    This class inherits from BaseGeometry and includes methods for calculating
    the area of the rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        area(self): Calculates the area of the rectangle.
    """
```

**Attributes:**

- `__width` (int): Represents the width of the rectangle. It is a private attribute and cannot be directly accessed from outside the class.
- `__height` (int): Represents the height of the rectangle. Like `__width`, it is private and cannot be directly accessed.

**Methods:**

1. `area(self)`: This method calculates and returns the area of the rectangle, which is the product of its width and height.

**Usage:**

The `Rectangle` class allows you to create instances of rectangles, providing width and height attributes. You can then use the `area` method to calculate the area of the rectangle.

**Example:**

```python
# Import the Rectangle class
Rectangle = __import__('9-rectangle').Rectangle

# Create an instance of the Rectangle class with width and height
r = Rectangle(3, 5)

# Calculate and print the area of the rectangle
print(r.area())
```

**Output:**

```
15
```


##Task 10 Documentation: Square Class Derived from Rectangle

**Description:**

In Task 10, we introduce the `Square` class, which is a specialization of the `Rectangle` class introduced in Task 9. A square is a special type of rectangle where all sides are equal in length. The `Square` class inherits attributes and methods from the `Rectangle` class while enforcing the additional constraint that width and height must be the same.

**Class Definition:**

```python
class Square(Rectangle):
    """
    A class representing a square, which is a special type of rectangle.

    This class inherits from the Rectangle class and enforces that both width
    and height are the same (i.e., the square is defined by a single side length).

    Attributes:
        __size (int): The side length of the square.

    Methods:
        area(self): Calculates the area of the square.
    """
```

**Attributes:**

- `__size` (int): Represents the side length of the square. It is a private attribute and cannot be directly accessed from outside the class.

**Methods:**

1. `area(self)`: This method calculates and returns the area of the square, which is the square of its side length.

**Usage:**

The `Square` class allows you to create instances of squares by providing a side length (size) as an attribute. You can then use the `area` method to calculate the area of the square.

**Example:**

```python
# Import the Square class
Square = __import__('10-square').Square

# Create an instance of the Square class with a side length (size)
s = Square(13)

# Calculate and print the area of the square
print(s.area())
```

**Output:**

```
169
```


##Task 11 Documentation: Square Class Derived from Rectangle (String Representation)

**Description:**

In Task 11, we extend the `Square` class introduced in Task 10, which is a specialization of the `Rectangle` class. A square is a special type of rectangle with all sides equal in length. In this task, we enhance the class by defining its string representation.

**Class Definition:**

```python
class Square(Rectangle):
    """
    A class representing a square, which is a special type of rectangle.

    This class inherits from the Rectangle class and enforces that both width
    and height are the same (i.e., the square is defined by a single side length).

    Attributes:
        __size (int): The side length of the square.

    Methods:
        area(self): Calculates the area of the square.
    """
```

**Attributes:**

- `__size` (int): Represents the side length of the square. It is a private attribute and cannot be directly accessed from outside the class.

**Methods:**

1. `area(self)`: This method calculates and returns the area of the square, which is the square of its side length.

2. `__str__(self)`: This is a special method that defines the string representation of the `Square` object. It returns a string in the format "[Square] <width>/<height>", where width and height are both equal to the side length.

**Usage:**

The `Square` class allows you to create instances of squares by providing a side length (size) as an attribute. You can then use the `area` method to calculate the area of the square. The `__str__` method defines how a `Square` object is represented as a string.

**Example:**

```python
# Import the Square class
Square = __import__('11-square').Square

# Create an instance of the Square class with a side length (size)
s = Square(13)

# Print the square using its string representation
print(s)
```

**Output:**

```
[Square] 13/13
```


##Task 12 Documentation: Custom MyInt Class with Inverted Comparison Operators

**Description:**

In Task 12, we define a custom class called `MyInt` that inherits from the built-in `int` class. The unique feature of the `MyInt` class is that it inverts the behavior of the equality (`==`) and inequality (`!=`) operators.

**Class Definition:**

```python
class MyInt(int):
    """
    A custom class that inherits from the int class with inverted comparison operators.

    Attributes:
        Inherited from the int class.

    Methods:
        None
    """
```

**Methods:**

The `MyInt` class does not define any new methods. It inherits all methods from the built-in `int` class.

**Operator Overloading:**

The distinctive feature of the `MyInt` class is that it inverts the behavior of the following comparison operators:

1. `==`: Normally, this operator checks if two objects are equal. In the `MyInt` class, it is overridden to check if two objects are not equal.

2. `!=`: Normally, this operator checks if two objects are not equal. In the `MyInt` class, it is overridden to check if two objects are equal.

**Usage:**

You can create instances of the `MyInt` class just like you would with the built-in `int` class. The primary difference is in how the `==` and `!=` operators behave. In the `MyInt` class, they have the opposite behavior compared to the standard `int` class.

**Example:**

```python
# Import the MyInt class
MyInt = __import__('100-my_int').MyInt

# Create an instance of the MyInt class
my_i = MyInt(3)

# Check if my_i is equal to 3 (opposite behavior)
print(my_i == 3)  # Outputs: False

# Check if my_i is not equal to 3 (opposite behavior)
print(my_i != 3)  # Outputs: True
```


##Task 13 Documentation: Add Attribute Function

**Description:**

Task 13 involves implementing a function called `add_attribute` that adds a new attribute to an object if it is possible to do so. If the object cannot have new attributes, the function raises a `TypeError` exception with the message "can't add new attribute."

**Function Definition:**

```python
def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attr_name (str): The name of the new attribute.
        attr_value (any): The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
```

**Parameters:**

- `obj` (object): The object to which the attribute should be added.
- `attr_name` (str): The name of the new attribute.
- `attr_value` (any): The value of the new attribute.

**Function Behavior:**

- The `add_attribute` function attempts to add a new attribute, given its name and value, to the provided object `obj`.

- If the object `obj` cannot have new attributes (i.e., it's not possible to dynamically add attributes to it), the function raises a `TypeError` exception with the message "can't add new attribute."

**Usage:**

You can use the `add_attribute` function to try to add new attributes to objects. If the object allows this operation, the attribute will be added. Otherwise, a `TypeError` exception will be raised.

**Examples:**

1. Adding an attribute to an object that allows it:

```python
# Create an object
obj = {}

# Attempt to add a new attribute to the object
add_attribute(obj, "name", "John")

# Access the new attribute
print(obj.name)  # Outputs: "John"
```

2. Attempting to add an attribute to an object that does not allow it:

```python
# Create a string object
my_string = "Hello, World!"

# Attempt to add a new attribute to the string (will raise an exception)
add_attribute(my_string, "name", "Bob")
```

In the first example, the `add_attribute` function successfully adds a new attribute to the dictionary object. In the second example, attempting to add an attribute to a string object results in a `TypeError` exception, as strings do not allow adding new attributes.
