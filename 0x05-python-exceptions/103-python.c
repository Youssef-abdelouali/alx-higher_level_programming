#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double _value_ = 0;
	char *_string_ = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	_value_ = ((PyFloatObject *)p)->ob_fval;
	_string_ = PyOS_double_to_string(_value_, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", _string_);
}
/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t _size_ = 0, a = 0;
	char *_string_ = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	_size_ = PyBytes_Size(p);
	printf("  size: %zd\n", _size_);
	_string_ = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", _string_);
	printf("  first %zd bytes:", _size_ < 10 ? _size_ + 1 : 10);
	do
	{
		printf(" %02hhx", _string_[a]);
		a++;
	} while (a < _size_ + 1 && a < 10);
	printf("\n");
}

/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t _size_ = 0;
	PyObject *_item_;
	int a = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		_size_ = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", _size_);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		do
		{
			_item_ = PyList_GET_ITEM(p, a);
			printf("Element %d: %s\n", a, Py_TYPE(_item_)->tp_name);
			if (PyBytes_Check(_item_))
				print_python_bytes(_item_);
			else if (PyFloat_Check(_item_))
				print_python_float(_item_);
			a++;
		} while (a < _size_);
	}
	else
		printf("[ERROR] Invalid List Object\n");
}
