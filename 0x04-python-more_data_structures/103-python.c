#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints bytes
 * @p: PyObject pointer
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *bytes;
	long int size, x, lmt;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = ((PyBytesObject *)p)->ob_sval;
	size = ((PyVarObject *)(p))->ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	if (size >= 10)
		lmt = 10;
	else
		lmt = size + 1;
	printf("  first %ld bytes:", lmt)
	for (x = 0; x < size && x < 10)
	{
		if (bytes[x] >= 0)
			printf(" %02x", bytes[x]);
		else
			printf(" %02x", 256 + bytes[x]);
	}
	printf("\n");
}

/**
 * print_python_list - prints info about python
 * @p: PyObject Pointer
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyObject *itm;
	long int size, x;
	PyListObject *l;

	size = ((PyVarOjbect *)(p))->ob_size;
	l = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List - %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (x = 0; x < size; x++)
	{
		itm = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((itm)->ob_type)->tp_name);
		if (PyBytes_Check(itm))
			print_python_bytes(itm);
	}
}

