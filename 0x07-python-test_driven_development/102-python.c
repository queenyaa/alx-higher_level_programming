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

/**
 * main - entry point
 * Return: 0 on success
 */
int main(void)
{
	Py_Initialize();

	/* Test cases */
	print_python_string(PyUnicode_DecodeUTF8("The spoon does not exist", \
				24, NULL));
	print_python_string(PyUnicode_DecodeUTF8("ложка не \
				существует", 19, NULL));
	print_python_string(PyUnicode_DecodeUTF8("La cuillère n'existe pas", \
				24, NULL));
	print_python_string(PyUnicode_DecodeUTF8("勺子不存在", 5, NULL));
	print_python_string(PyUnicode_DecodeUTF8("숟가락은 존재하지 \
				않는다.", 14, NULL));
	print_python_string(PyUnicode_DecodeUTF8("スプーンは存在しない", \
				10, NULL));
	print_python_string(NULL);  /* Invalid string object */

	Py_Finalize();
	return (0);
}
