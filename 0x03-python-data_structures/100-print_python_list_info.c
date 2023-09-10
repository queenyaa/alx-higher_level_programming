#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *itm;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (v = 0; v < list_size; v++)
	{
		itm = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", v, Py_TYPE(itm)->tp_name);
	}
}
