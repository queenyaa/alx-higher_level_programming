Readme of 0x05-python-exceptions

```
# CPython Tasks

This repository contains a set of CPython tasks that involve creating C functions to interact with Python objects using the Python C API.

## Prerequisites

Before attempting the tasks, ensure you have the following installed on your system:

- Python (CPython)
- A C compiler (e.g., GCC)

## Task Descriptions

### Task 1: Print Elements of a List

- Function: `void print_python_list(PyObject *p)`
- Description: Print information about a Python list.
- Format: See example in the code.
- Error Handling: Print an error message if `p` is not a valid PyListObject.

### Task 2: Print Elements of Bytes

- Function: `void print_python_bytes(PyObject *p)`
- Description: Print information about a Python bytes object.
- Format: See example in the code.
- Error Handling: Print an error message if `p` is not a valid PyBytesObject.

### Task 3: Print Python Float

- Function: `void print_python_float(PyObject *p)`
- Description: Print information about a Python float object.
- Format: See example in the code.
- Error Handling: Print an error message if `p` is not a valid PyFloatObject.

### Task 4: Print Elements of a List (Advanced)

- Function: `void print_python_list(PyObject *p)`
- Description: Print information about a Python list with advanced error handling.
- Format: See example in the code.
- Error Handling: Handle various error conditions as described in the code.

### Task 5: Print Python Bytes (Advanced)

- Function: `void print_python_bytes(PyObject *p)`
- Description: Print information about a Python bytes object with advanced error handling.
- Format: See example in the code.
- Error Handling: Handle various error conditions as described in the code.

### Task 6: Print Python Float (Advanced)

- Function: `void print_python_float(PyObject *p)`
- Description: Print information about a Python float object with advanced error handling.
- Format: See example in the code.
- Error Handling: Handle various error conditions as described in the code.

### Task 7: Safe Print Integer

- Function: `void safe_print_integer_err(PyObject *p)`
- Description: Print an integer value and handle exceptions.
- Format: See example in the code.
- Error Handling: Print an error message if the value is not an integer.

### Task 8: Safe Execute Function

- Function: `PyObject *safe_function(PyObject *p, char *name, PyObject *args)`
- Description: Execute a Python function safely and handle exceptions.
- Error Handling: Print an error message if an exception occurs during the function execution.

## Usage

You can compile and run the C code for each task to test the functions. Refer to the task-specific code for examples and usage instructions.

```bash
gcc -o task1 task1.c -I/usr/include/python3.X -lpython3.X
./task1
```

Replace task1 with the appropriate task filename.
