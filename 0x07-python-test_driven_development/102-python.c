#include <Python.h>

/**
 * print_python_string - function to print Python strings
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t py_len;
	char *str;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		py_len = PyUnicode_GET_LENGTH(p);
		str = PyBytes_AsString(PyUnicode_AsUTF8String(p));
		if (PyUnicode_IS_COMPACT_ASCII(p))
			 printf("  type: compact ascii%s\n");
		else
			 printf("  type: compact unicode object%s\n");
		printf("  length: %zd\n  value: %s\n", py_len, str);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
	fflush(stdout);
}
