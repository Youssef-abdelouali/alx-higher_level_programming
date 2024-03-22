#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    long int list_size = PyList_Size(p);
    int index;
    PyListObject *list_obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", list_size);
    printf("[*] Allocated = %li\n", list_obj->allocated);
    for (ix = 0; ix < list_size; ix++)
        printf("Element %i: %s\n", ix, Py_TYPE(list_obj->ob_item[ix])->tp_name);
}
