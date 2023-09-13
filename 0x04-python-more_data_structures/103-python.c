#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints info about python
 * @p: PyObject Pointer
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyObject *itm;
	Py_ssize_t size, x;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List - %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (x = 0; x < size; x++)
	{
		itm = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints bytes
 * @p: PyObject pointer
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	PyObject *bytes;
	Py_ssize_t size, x;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyObject *)((PyvarObject *)p + 1);
	size = PyBytes_GET_SIZE(p);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", PyUnicode_AsUTF8(bytes));
	printf("  [.] first %ld bytes: ", (size < 10) ? size + 1 : 10);

	for (x = 0; x < size && x < 10)
	{
		printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[x]);
		if (x + 1 < size && x + 1 < 10)
			printf(" ");
	}
	printf("\n");
}
