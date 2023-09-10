Readme of 0x03-python-data_structures


```markdown
# CPython and Python Tasks

This repository contains a collection of tasks related to CPython and Python programming. Each task is a separate function or code snippet that demonstrates various aspects of Python programming and interaction with CPython.

## Table of Contents

- [Task 0: Print List of Integers](#task-0-print-list-of-integers)
- [Task 1: Retrieve Element from List](#task-1-retrieve-element-from-list)
- [Task 2: Replace Element in List](#task-2-replace-element-in-list)
- [Task 3: Print Reversed List of Integers](#task-3-print-reversed-list-of-integers)
- [Task 4: Replace Element in List (Immutable)](#task-4-replace-element-in-list-immutable)
- [Task 5: Remove Characters from String](#task-5-remove-characters-from-string)
- [Task 6: Print Matrix of Integers](#task-6-print-matrix-of-integers)
- [Task 7: Add Two Tuples](#task-7-add-two-tuples)
- [Task 8: Return Length and First Character of String](#task-8-return-length-and-first-character-of-string)
- [Task 9: Find the Biggest Integer in a List](#task-9-find-the-biggest-integer-in-a-list)
- [Task 10: Find Multiples of 2 in a List](#task-10-find-multiples-of-2-in-a-list)
- [Task 11: Delete Item at Specific Position in a List](#task-11-delete-item-at-specific-position-in-a-list)
- [Task 13: Check if Singly Linked List is a Palindrome](#task-13-check-if-singly-linked-list-is-a-palindrome)

## Task 0: Print List of Integers

- Prototype: `def print_list_integer(my_list=[])`
- Description: This function prints all integers in a list, one integer per line.

## Task 1: Retrieve Element from List

- Prototype: `def element_at(my_list, idx)`
- Description: This function retrieves an element from a list at a specific index. It returns `None` if the index is negative or out of range.

## Task 2: Replace Element in List

- Prototype: `def replace_in_list(my_list, idx, element)`
- Description: This function replaces an element in a list at a specific position (similar to C). It returns the original list if the index is negative or out of range.

## Task 3: Print Reversed List of Integers

- Prototype: `def print_reversed_list_integer(my_list=[])`
- Description: This function prints all integers in a list in reverse order, one integer per line.

## Task 4: Replace Element in List (Immutable)

- Prototype: `def new_in_list(my_list, idx, element)`
- Description: This function replaces an element in a list at a specific position without modifying the original list (similar to C). It returns a copy of the original list if the index is negative or out of range.

## Task 5: Remove Characters from String

- Prototype: `def no_c(my_string)`
- Description: This function removes all occurrences of the characters 'c' and 'C' from a string and returns the new string.

## Task 6: Print Matrix of Integers

- Prototype: `def print_matrix_integer(matrix=[[]])`
- Description: This function prints a matrix of integers in a specified format.

## Task 7: Add Two Tuples

- Prototype: `def add_tuple(tuple_a=(), tuple_b=())`
- Description: This function adds two tuples and returns a tuple with two integers, where the first element is the addition of the first element of each argument and the second element is the addition of the second element of each argument.

## Task 8: Return Length and First Character of String

- Prototype: `def multiple_returns(sentence)`
- Description: This function returns a tuple with the length of a string and its first character. If the sentence is empty, the first character is `None`.

## Task 9: Find the Biggest Integer in a List

- Prototype: `def max_integer(my_list=[])`
- Description: This function finds and returns the biggest integer in a list. It returns `None` if the list is empty.

## Task 10: Find Multiples of 2 in a List

- Prototype: `def divisible_by_2(my_list=[])`
- Description: This function returns a new list with `True` or `False` values, depending on whether each integer in the original list is a multiple of 2.

## Task 11: Delete Item at Specific Position in a List

- Prototype: `def delete_at(my_list=[], idx=0)`
- Description: This function deletes the item at a specific position in a list. If the index is negative or out of range, it does

 nothing and returns the same list.

## Task 13: Check if Singly Linked List is a Palindrome

- Prototype: `int is_palindrome(listint_t **head)`
- Description: This function checks if a singly linked list is a palindrome and returns `0` if it is not a palindrome or `1` if it is. An empty list is considered a palindrome.

## Task 14: CPython and Python Lists

- Description: Create a C function named `print_python_list_info` that prints basic information about Python lists, such as their size, allocated memory, and the type of elements they contain. The function interacts with Python's C API and provides insight into how Python lists work internally.

## Usage

To use these functions, you can import them into your Python code and call them as needed.

```python
from tasks import print_list_integer, element_at, replace_in_list, ...
```


