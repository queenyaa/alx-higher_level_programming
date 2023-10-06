#include "Python.h"
#include <stdio.h>

/**
 * print_python_string - function to print Python strings
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
	Py_UNICODE *value = PyUnicode_AsUnicode(p);
	char *value = PyString_AsString(p);

	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		
		if (value)
		{
			wprintf(L"  value: %ls\n, value");
		}
	}
	else if (PyString_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", PyString_GET_SIZE(p));

		if (value)
		{
			printf("  value: %s\n", value);
		}
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
