#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes_info - Prints information about bytes objects.
 * @p: Python bytes object.
 *
 * Description: This function prints size, content, and hexadecimal representation
 * of the first 10 bytes of a Python bytes object.
 */
void print_python_bytes_info(PyObject *p)
{
    char *bytes_str;
    long int size, i, limit;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    bytes_str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_str);

    limit = size >= 10 ? 10 : size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
    {
        if (bytes_str[i] >= 0)
            printf(" %02x", bytes_str[i]);
        else
            printf(" %02x", 256 + bytes_str[i]);
    }

    printf("\n");
}

/**
 * print_python_list_info - Prints information about Python lists.
 * @p: Python list object.
 *
 * Description: This function prints the size, allocated memory, and types of
 * elements in the Python list. If an element is a bytes object, it calls
 * print_python_bytes_info to print additional information.
 */
void print_python_list_info(PyObject *p)
{
    long int list_size, i;
    PyListObject *list;
    PyObject *obj;

    list_size = ((PyVarObject *)p)->ob_size;
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < list_size; i++)
    {
        obj = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

        if (PyBytes_Check(obj))
            print_python_bytes_info(obj);
    }
}
