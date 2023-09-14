Readme of 0x04-python-more_data_structures


```
# Python C Tasks README

This README provides an overview of the tasks and their requirements for Python C programming.

## General Requirements

- All code is expected to work with Python 3.4.
- Compilation command for shared library: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`.
- Avoid using disallowed macros/functions mentioned in the task descriptions.
- Ensure the code is properly formatted and readable.

## Task 0 - Square Matrix Calculation

Write a function `square_matrix_simple` to compute the square value of all integers in a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- Use regular loops, map, etc., without importing any modules.

## Task 1 - Search and Replace in a List

Write a function `search_replace` to replace all occurrences of an element with another in a list.

- Prototype: `def search_replace(my_list, search, replace):`
- Do not import any modules.

## Task 2 - Unique Sum in a List

Write a function `uniq_add` to add all unique integers in a list.

- Prototype: `def uniq_add(my_list=[]):`
- Do not import any modules.

## Task 3 - Find Common Elements in Sets

Write a function `common_elements` to find common elements between two sets.

- Prototype: `def common_elements(set_1, set_2):`
- Do not import any modules.

## Task 4 - Find Elements in Only One Set

Write a function `only_diff_elements` to find elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2):`
- Do not import any modules.

## Task 5 - Count Keys in a Dictionary

Write a function `number_keys` to count the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`
- Do not import any modules.

## Task 6 - Print Sorted Dictionary

Write a function `print_sorted_dictionary` to print a dictionary with keys sorted alphabetically.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- Do not import any modules.

## Task 7 - Update or Add Key-Value Pair

Write a function `update_dictionary` to update or add a key-value pair in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value):`
- Do not import any modules.

## Task 8 - Simple Key Deletion

Write a function `simple_delete` to delete a key from a dictionary.

- Prototype: `def simple_delete(a_dictionary, key=""):`
- Do not import any modules.

## Task 9 - Multiply Dictionary Values by 2

Write a function `multiply_by_2` to create a new dictionary with all values multiplied by 2.

- Prototype: `def multiply_by_2(a_dictionary):`
- Do not import any modules.

## Task 10 - Find Key with the Largest Value

Write a function `best_score` to find and return the key with the largest integer value in a dictionary.

- Prototype: `def best_score(a_dictionary):`
- Do not import any modules.

## Task 11 - Multiply List Elements by a Number

Write a function `multiply_list_map` to create a new list with all values multiplied by a number using `map`.

- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Use `map` and do not import any modules.

## Task 12 - Convert Roman Numerals to Integer

Write a function `roman_to_int` to convert a Roman numeral to an integer.

- Prototype: `def roman_to_int(roman_string):`
- Handle numbers between 1 to 3999.
- Return an integer, or 0 if the input is not a valid Roman numeral.

## Task 13 - Weighted Average of Tuples

Write a function `weight_average` to calculate the weighted average of integer tuples.

- Prototype: `def weight_average(my_list=[]):`
- Return 0 if the list is empty.
- Do not import any modules.

## Task 14 - Square Matrix Calculation with Map

Write a function `square_matrix_map` to compute the square value of all integers in a matrix using `map`.

- Prototype: `def square_matrix_map(matrix=[]):`
- Use `map` and do not import any modules.
- Do not use loops.

## Task 15 - Delete Keys with Specific Value

Write a function `complex_delete` to delete keys with a specific value in a dictionary.

- Prototype: `def complex_delete(a_dictionary, value):`
- Do not import any modules.

## Task 16 - Print Python Lists and Bytes

Create C functions that print information about Python lists and bytes objects.

- `print_python_list(PyObject *p)` to print information about Python lists.
- `print_python_bytes(PyObject *p)` to print information about Python bytes objects.
- Follow the specified formats.
- Do not use disallowed macros/functions.

Feel free to refer to individual task sections for more details on each task.

```

This README provides a high-level overview of all the tasks and their requirements. For detailed information on each task, please refer to the corresponding section in the README.
