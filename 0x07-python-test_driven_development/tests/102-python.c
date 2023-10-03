#include <Python.h>

/**
 * print_python_string - function to print Python strings
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: %s\n", Py_TYPE(p)->tp_name);
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
