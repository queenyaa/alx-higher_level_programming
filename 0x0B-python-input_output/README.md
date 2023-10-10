Readme of 0x0B-python-input_output


---

**Task 0**

**Objective:**
The goal of this task is to create a Python script that reads input from the standard input (stdin) and prints it to the standard output (stdout).

**Script Description:**
- The script uses a function named `read_file` to read lines from the standard input.
- It reads each line from stdin and prints it to stdout.

**Usage:**
1. To run the script, execute it in a terminal or command prompt using the Python interpreter. For example:
   ```
   python 0-read_file.py
   ```

2. Input lines from the standard input. The script will immediately print each line back to the standard output.

3. To exit the script and return to the command prompt, press `Ctrl + D` (Linux/Unix) or `Ctrl + Z` followed by Enter (Windows).

**Example:**
Suppose you run the script and provide the following input lines:

```
Hello, World!
This is a test.
Python is great.
```

The script will print these lines to the standard output:

```
Hello, World!
This is a test.
Python is great.
```

**Notes:**
- This script serves as a basic demonstration of reading input from stdin and writing to stdout in Python.
- It can be useful for various applications where you need to process and display input from the user or other sources.

---



**Task 1: Create a function that prints a text with 2 new lines after each of these characters: `., ? and :`**

**Function Signature:** `def text_indentation(text)`

### Description:

The goal of this task is to create a Python function that takes a string of text as input and adds two new lines after each occurrence of the characters `., ?`, and `:` in the input text. The modified text should then be printed as the output.

### Input:

- `text` (str): A string of text containing sentences and punctuations.

### Output:

- The function does not return any value. It prints the modified text with two new lines after each occurrence of the characters `., ?`, and `:`.

### Example:

```python
text_indentation("This is a simple text. With some sentences: Are they separated by two new lines?") 

# Output:
# This is a simple text.
#
# With some sentences:
#
# Are they separated by two new lines?
```

### Constraints:

- The input text will contain at least one character.
- The input text may contain multiple spaces.
- The input text may contain multiple sentences and punctuations.

---


**Task 3: Create a Function to Convert Objects to JSON Strings**

**Function Signature:** `def to_json_string(my_obj)`

### Description:

The goal of this task is to create a Python function that takes an object (`my_obj`) as input and returns its JSON representation as a string. The function uses the `json.dumps()` method to convert the input object to a JSON string.

### Input:

- `my_obj`: The input object to be converted to a JSON string.

### Output:

- The function returns a JSON string representation of the input object.

### Example:

```python
if __name__ == "__main__":
    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))

    my_dict = { 
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    s_my_dict = to_json_string(my_dict)
    print(s_my_dict)
    print(type(s_my_dict))

# Output:
# [1, 2, 3]
# <class 'str'>
# {"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}
# <class 'str'>
```

### Constraints:

- The input object (`my_obj`) must be serializable to JSON (e.g., lists, dictionaries, strings, numbers, and boolean values).

---



**Task 4: Create a Function to Parse JSON Strings into Python Objects**

**Function Signature:** `def from_json_string(my_str)`

### Description:

The goal of this task is to create a Python function that takes a JSON string (`my_str`) as input and returns the equivalent Python data structure. The function uses the `json.loads()` method to parse the JSON string and convert it into a Python object.

### Input:

- `my_str`: A JSON string to be parsed into a Python object.

### Output:

- The function returns the Python data structure obtained from parsing the input JSON string.

### Example:

```python
if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14}, 
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

# Output:
# [1, 2, 3]
# <class 'list'>
# {'is_active': True, 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'name': 'John', 'places': ['San Francisco', 'Tokyo']}
# <class 'dict'>
```

### Constraints:

- The input JSON string (`my_str`) must be well-formed and represent a valid JSON data structure.

---



**Task 5: Create a Function to Save Python Objects to a JSON File**

**Function Signature:** `def save_to_json_file(my_obj, filename)`

### Description:

The goal of this task is to create a Python function that writes a Python object (`my_obj`) to a text file using its JSON representation. The function uses the `json.dump()` method to serialize the object into a JSON-formatted string and save it to the specified file.

### Inputs:

- `my_obj`: The Python object to be saved.
- `filename`: The name of the file where the JSON representation of the object will be stored.

### Outputs:

- The function does not return any values. It saves the JSON representation of the object to the specified file.

### Example:

```python
if __name__ == "__main__":
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = { 
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

# Output:
# Two JSON files, 'my_list.json' and 'my_dict.json', are created with the respective JSON representations of the objects.
```

### Constraints:

- The `my_obj` should be serializable to JSON.
- The `filename` should be a valid and writable file path.

---


**Task 6: Create a Function to Load Objects from a JSON File**

**Function Signature:** `def load_from_json_file(filename)`

### Description:

The goal of this task is to create a Python function that reads a JSON file and creates a Python object from its contents. The function uses the `json.load()` method to deserialize the JSON data from the specified file and returns the resulting Python object.

### Inputs:

- `filename`: The name of the JSON file to be read.

### Outputs:

- The function returns the Python object created from the JSON data in the file.

### Example:

```python
if __name__ == "__main__":
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

# Output:
# The loaded objects and their types are printed. If the file doesn't exist or if there's an issue with the JSON data, it handles exceptions gracefully.
```

### Constraints:

- The file specified in `filename` should exist and be a valid JSON file.
- The function can load objects that are serializable to JSON.

---


**Task 7: Save and Load Items to/from a JSON File**

**Main Script**

The main script aims to manage a list of items stored in a JSON file. It allows you to add items to this list and save the updated list back to the JSON file. The list is represented by a JSON array.

### Description:

- **save_to_json_file(my_obj, filename):**
  - This function takes an object `my_obj` and a filename as inputs. The purpose of this function is to save the content of `my_obj` to a JSON file specified by `filename`. It uses the `json.dump()` method to serialize the object to a JSON representation and write it to the file.

- **load_from_json_file(filename):**
  - This function reads the content of a JSON file specified by `filename` and deserializes it into a Python object. It returns the deserialized object. If the file doesn't exist, it returns an empty list.

- **sys.argv[1:]:**
  - It extracts the command-line arguments starting from the second argument (index 1). These arguments are assumed to be items to add to the list.

- **Managing the List:**
  - Initially, it attempts to load the list of items from a file named "add_item.json." If the file doesn't exist, it initializes an empty list.

- **Adding Items:**
  - The command-line arguments (provided by `sys.argv[1:]`) are considered items to add to the list. These items are added to the list using the `extend` method.

- **Saving the Updated List:**
  - After adding the items to the list, it calls `save_to_json_file` to save the updated list back to the "add_item.json" file.

### Example:

```python
# Assuming the script is called with additional arguments
# ./7-add_item.py item1 item2 item3

# File "add_item.json" will be created (if it doesn't exist) or updated with the following contents:
# ["item1", "item2", "item3"]
```

### Constraints:

- The script uses `json` for serialization and deserialization, so it can handle objects that are serializable to JSON.

---


---

**Task 8: Serialize a Class Instance to a JSON-Convertible Dictionary**

### Description:

The function `class_to_json(obj)` is designed to take an instance of a class as input and return a dictionary representation of that instance. This representation can be easily serialized to JSON format. The function works as follows:

- `obj_dict = obj.__dict__.copy()`: It first creates a copy of the instance dictionary (`__dict__`) to capture all the attributes and their values of the class instance.

- Handling Private Attributes: In Python, private attributes can be present in the class, and they are often subject to name mangling, which changes their names to include the class name as a prefix. To ensure that private attributes are correctly represented in the resulting dictionary, the function performs the following steps:

  - It iterates through the keys of the copied dictionary (`obj_dict`).

  - For keys that start with `'_' + obj.__class__.__name__ + '__'`, the function creates a new key by removing the name mangling part. This ensures that private attributes are not lost during serialization.

### Purpose:

The purpose of this function is to provide a way to serialize instances of a class into a format that can be easily converted to JSON. It is especially useful when you want to save the state of an object to a file, transmit it over a network, or store it in a database in a structured format.

### Example:

```python
class MyClass:
    def __init__(self, name):
        self.name = name
        self._score = 100
        self.__private_var = "Secret"

m = MyClass("John")
json_representation = class_to_json(m)
```

In the above example, `json_representation` will be a dictionary containing the attributes of the `MyClass` instance `m`, including the private attribute `_score`, with the name mangling removed.

### Notes:

- The function does not handle recursive objects, and it assumes that the object's attributes are serializable to JSON.

- The resulting dictionary can be passed to the `json.dump()` function to save it to a JSON file or be further processed for other purposes.

---


---

**Task 9: Create a Student Class for JSON Serialization**

### Description:

The `Student` class is designed to represent a student with the following attributes: `first_name`, `last_name`, and `age`. This class provides the following methods:

- `__init__(self, first_name, last_name, age)`: This method serves as the constructor for the `Student` class. It initializes a `Student` instance with the provided `first_name`, `last_name`, and `age` attributes.

- `to_json(self)`: This method retrieves a dictionary representation of the `Student` instance. It creates and returns a dictionary with keys `'first_name'`, `'last_name'`, and `'age'`, which correspond to the attributes of the student.

### Purpose:

The purpose of the `Student` class is to encapsulate student information and provide a standardized way to retrieve a JSON-serializable representation of a student. This can be useful when you need to convert student data into JSON format for storage, transmission, or processing.

### Example:

```python
# Create a Student instance
student = Student("John", "Doe", 25)

# Retrieve a JSON-serializable dictionary representation
student_json = student.to_json()
```

In the above example, `student_json` will be a dictionary with the following structure:

```json
{
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25
}
```

This representation can be easily converted to a JSON string.

### Notes:

- The `to_json` method provides a structured way to retrieve a dictionary of student information. This can be helpful in scenarios where you need to work with JSON data in Python.

- The class assumes that `first_name`, `last_name`, and `age` are always provided during the instance's initialization.

---


---

**Task 10: Enhancing the Student Class for JSON Serialization with Attribute Filtering**

### Description:

The `Student` class is designed to represent a student with the following attributes: `first_name`, `last_name`, and `age`. This class provides the following methods:

- `__init__(self, first_name, last_name, age)`: This method serves as the constructor for the `Student` class. It initializes a `Student` instance with the provided `first_name`, `last_name`, and `age` attributes.

- `to_json(self, attrs=None)`: This method retrieves a dictionary representation of the `Student` instance. It can optionally filter the attributes to include in the dictionary by passing a list of attribute names as `attrs`. If `attrs` is `None`, it includes all attributes. If an attribute exists in the student instance and is in `attrs`, it is included in the result.

### Purpose:

The purpose of this enhanced `Student` class is to provide more flexibility for JSON serialization. By allowing attribute filtering, it's possible to specify which student attributes should be included in the JSON representation. This can be useful when you need to create customized JSON representations of student data.

### Example:

```python
# Create a Student instance
student = Student("John", "Doe", 25)

# Retrieve a JSON-serializable dictionary representation with selected attributes
selected_attrs = ['first_name', 'age']
student_json = student.to_json(selected_attrs)
```

In the above example, `student_json` will be a dictionary with the following structure:

```json
{
    'first_name': 'John',
    'age': 25
}
```

This representation includes only the attributes specified in `selected_attrs`.

### Notes:

- The ability to filter attributes allows for more precise control over the JSON representation of a `Student` instance.

- The class assumes that `first_name`, `last_name`, and `age` are always provided during the instance's initialization.

- If the `attrs` parameter is `None`, all attributes are included in the dictionary.

- Attributes not present in the instance are gracefully ignored.

---


---

**Task 11: Expanding the Student Class with JSON Serialization and Deserialization**

### Description:

The `Student` class is designed to represent a student with attributes such as `first_name`, `last_name`, and `age`. This class provides the following methods:

- `__init__(self, first_name, last_name, age)`: This method is the constructor for the `Student` class, initializing an instance with the provided `first_name`, `last_name`, and `age`.

- `to_json(self, attrs=None)`: This method retrieves a dictionary representation of the `Student` instance, with optional attribute filtering. If `attrs` is not specified or is `None`, it returns a dictionary containing all attributes. If `attrs` is provided, it filters the attributes to include based on the list.

- `reload_from_json(self, json)`: This method replaces all attributes of the `Student` instance with values from a dictionary (`json`). It updates the student's attributes with the corresponding values from the dictionary.

### Purpose:

The enhanced `Student` class serves two purposes:

1. JSON Serialization: It allows the conversion of a `Student` instance into a JSON-serializable dictionary. This is useful when you need to convert student data into a format that can be easily stored or transmitted.

2. JSON Deserialization: It facilitates the creation of a `Student` instance from a JSON representation. This is valuable when you want to recreate a `Student` object from JSON data.

### Example:

```python
# Create a Student instance
student = Student("John", "Doe", 25)

# Retrieve a JSON-serializable dictionary representation with selected attributes
selected_attrs = ['first_name', 'age']
student_json = student.to_json(selected_attrs)

# Recreate the student instance from a JSON dictionary
new_student = Student("Jane", "Smith", 22)
new_student.reload_from_json(student_json)
```

In this example, `new_student` will have its attributes updated to match the values from the `student_json` dictionary.

### Notes:

- The `reload_from_json` method can be used to reassign attributes from a dictionary representation.

- The class assumes that `first_name`, `last_name`, and `age` are always provided during the instance's initialization.

- Attribute filtering in `to_json` allows for more precise control over the JSON representation of a `Student` instance.

- When using `reload_from_json`, make sure the dictionary keys match the attribute names, and the values are of the correct types.

---


---

**Task 12: Generating Pascal's Triangle**

### Description:

The `pascal_triangle` function generates Pascal's triangle with a specified number of rows (`n`). Pascal's triangle is a triangular array of binomial coefficients, used in various mathematical and combinatorial problems. It starts with a single "1" at the top and expands downward, where each number is obtained by adding the two numbers above it.

### Function Signature:

```python
def pascal_triangle(n):
```

### Parameters:

- `n` (int): Number of rows to generate in Pascal's triangle.

### Returns:

- `list of lists`: A representation of Pascal's triangle containing `n` rows.

### Algorithm:

1. Initialize an empty list, `triangle`, to store the rows of Pascal's triangle.

2. Check if `n` is less than or equal to 0. If `n` is not a positive integer, return an empty list as Pascal's triangle cannot be generated with zero or negative rows.

3. Initialize the `triangle` with the first row, which contains a single "1."

4. Iterate from the second row to the `n`-th row, generating each row based on the previous row.

5. For each row, start with "1" (the first element) and then calculate the middle elements by adding the elements from the previous row.

6. Finish each row with "1" (the last element).

7. Append each row to the `triangle` list.

8. After generating all the rows, return the `triangle` as the Pascal's triangle representation.

### Example:

```python
triangle = pascal_triangle(5)
```

In this example, `triangle` will be a list of lists representing Pascal's triangle with 5 rows. Printing `triangle` will display:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

### Notes:

- Pascal's triangle is a useful mathematical construct with applications in combinatorics, probability theory, and algebra.

- The function handles the case where `n` is less than or equal to 0 by returning an empty list.

- You can use this function to generate Pascal's triangle with a specific number of rows, which can be helpful in various mathematical and programming tasks.

---


---

**Task 13: Inserting Text After Specific Lines in a File**

### Description:

The `append_after` function inserts a line of text after each line that contains a specific search string in a file. This can be useful for adding comments, annotations, or additional content to an existing file.

### Function Signature:

```python
def append_after(filename="", search_string="", new_string=""):
```

### Parameters:

- `filename` (str): The name of the file in which to perform the insertion.
- `search_string` (str): The string to search for in each line of the file.
- `new_string` (str): The string to insert after each line that contains the `search_string`.

### File Processing Algorithm:

1. Open the file specified by `filename` for reading (`'r'` mode) to read its content line by line. If the file does not exist, a `FileNotFoundError` exception is caught and ignored.

2. Read all the lines of the file into a list of strings called `lines`.

3. Open the same file for writing (`'w'` mode) to overwrite its content. This will effectively clear the file for rewriting.

4. Iterate through each line in the `lines` list:

   a. Write the current line to the file using the `file.write(line)` method, which retains the original content of each line.

   b. Check if `search_string` is present in the current line. If found, insert `new_string` after the line by calling `file.write(new_string)`.

5. Close the file after processing.

### Usage Example:

```python
append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
```

In this example, the function will open the file named "append_after_100.txt" and insert the string `\"C is fun!\"\n` after each line containing the string "Python." The original file's content will be preserved, and the modified content will be written back to the file.

### Notes:

- This function is a basic example of text file manipulation and can be used to automate simple text editing tasks.

- The original file's content will be preserved, and new content will be inserted after matching lines.

- The function handles the case where the specified file does not exist by catching and ignoring the `FileNotFoundError` exception.

---


---

**Task 14: Computing Metrics for Log Data**

### Description:

The script provided reads input from standard input (stdin), which is assumed to be in a specific log data format. It processes the data, computes statistics, and prints metrics every 10 lines of input or after receiving a keyboard interruption (CTRL + C).

### Script Purpose:

The script processes log data with the following format for each line:
`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

The script maintains and calculates the following metrics:

- `Total file size`: The sum of the file sizes from all previous lines.
- `Number of lines by status code`: The count of each status code (e.g., 200, 301, 400) encountered in the input. The status codes are sorted in ascending order.

### Function Signature:

The script doesn't have a specific function signature. It processes data in the `if __name__ == '__main__'` block.

### Algorithm:

1. Initialize a variable `tot` to 0, which will store the total file size.
2. Create a dictionary `stat_cd` with status codes (200, 301, 400, 401, 403, 404, 405, 500) as keys and initialize their values to 0.
3. Iterate over the lines read from standard input.
4. For each line, parse the file size and status code.
5. Update `tot` with the file size and increment the count of the corresponding status code in the `stat_cd` dictionary.
6. After processing every 10 lines, or when a keyboard interruption (CTRL + C) occurs, print the `Total file size` and the count of status codes.
7. Continue processing input until the script is interrupted.

### Usage Example:

The script can be executed as follows:
```bash
python script.py < input.log
```

Where `input.log` contains log data in the specified format.

### Notes:

- The script is designed for processing log data, counting status codes, and computing the total file size.

- It handles keyboard interruptions (CTRL + C) to provide intermediate and final statistics.

- The metrics are printed to the standard output for monitoring and analysis.

---
