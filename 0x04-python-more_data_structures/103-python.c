#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>

/**
 * print_python_bytes - prints bytes of python
 * @p: pointer to PyObject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int bytes, x;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		bytes = PyBytes_Size(p);
		prinf("  size: %ld\n", bytes);
		prntf("  trying string: %s\n", PyBytes_AsString(p));
		if (bytes >= 10)
			bytes = 10;
		else
			bytes++;
		printf("  first %ld bytes:", bytes);
		for (x = 0; x < bytes; x++)
			printf(" %02x", (int) PyBytes_AsString(p)[x] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - prints info
 * @p: pointer to PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int s_list = PyList_GET_SIZE(p), l_index;
	pyObject *tmp;
	PyListObject *l_obj = (PyListObject *) p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s_list);
	printf("[*] Allocated = %ld\n", l_obj->allocated);

	for (l_index = 0; l_index < s_list; l_index++)
	{
		temp = PyList_GET_ITEM(p, l_index);
		printf("Element %ld: %s\n", l_index,
				tmp->ob_type->tp_name);
		if (PyBytes_CheckExact(tmp))
			print_python_bytes(tmp);
	}
}
