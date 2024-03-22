#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *bytes_str;
	long int bytes_size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes_size = ((PyVarObject *)(p))->ob_size;
	bytes_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", bytes_str);

	if (bytes_size >= 10)
		limit = 10;
	else
		limit = bytes_size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (bytes_str[i] >= 0)
			printf(" %02x", bytes_str[i]);
		else
			printf(" %02x", 256 + bytes_str[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int list_size, i;
	PyListObject *list;
	PyObject *obj;

	list_size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
