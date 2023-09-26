#include <Python.h>

/**
 * print_python_bytes - basic info about python bytes
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sz, x;
	PyBytesObject *byt = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byt->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		sz = 10;
	else
		sz = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %ld bytes: ", sz);
	for (x = 0; x < sz; x++)
	{
		printf("%02hhx", byt->ob_sval[x]);
		if (x == (sz - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - basic info on Python floats
 * @p: PyObject float
 */
void print_python_float(PyObject *p)
{
	char *buf = NULL;

	PyFloatObject *f_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buf = PyOS_double_to_string(f_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}

/**
 * print_python_list - basic info printing
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t sz, aloc, x;
	const char *typ;
	PyListObject *lst = (PyListObject *)p;
	PyVarObject *v = (PyVarObject *)p;

	sz = v->ob_size;
	aloc = lst->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", aloc);

	for (x = 0; x < sz; x++)
	{
		typ = lst->ob_item[x]->ob_type->tp_name;
		printf("Element %ld: %s\n", x, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(lst->ob_item[x]);
		else if (strcmp(typ, "float") == 0)
			print_python_float(lst->ob_item[x]);
	}
}
