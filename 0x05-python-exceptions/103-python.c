#include <Python.h>
#include <stdio.h>

/* 
 * Function to print information about a Python list object.
 */
void print_python_list(PyObject *p)
{
    /* Ensure unbuffered output. */
    setbuf(stdout, NULL);

    /* Check if the object is a valid list. */
    if (!PyList_Check(p)) {
        printf("Invalid List object\n");
        return;
    }

    /* Print header information. */
    printf("[*] Python list info\n");

    /* Print object address. */
    printf("  address  : %p\n", p);

    /* Print list size and allocated memory. */
    printf("  size     : %ld\n", ((PyListObject *)p)->ob_size);
    printf("  allocated: %ld\n", ((PyListObject *)p)->allocated);
}

/* 
 * Function to print information about a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
    /* Ensure unbuffered output. */
    setbuf(stdout, NULL);

    /* Check if the object is a valid bytes object. */
    if (!PyBytes_Check(p)) {
        printf("Invalid Bytes object\n");
        return;
    }

    /* Print header information. */
    printf("[*] Python bytes info\n");

    /* Print object address. */
    printf("  address    : %p\n", p);

    /* Print object size. */
    printf("  size       : %ld\n", ((PyBytesObject *)p)->ob_base.ob_size);

    /* Print first 10 bytes or all bytes if less than 10. */
    printf("  first 10 bytes: ");
    fwrite(((PyBytesObject *)p)->ob_sval, 1,
           (((PyBytesObject *)p)->ob_base.ob_size > 10) ? 10 :
           ((PyBytesObject *)p)->ob_base.ob_size, stdout);
    printf("\n");
}

/* 
 * Function to print information about a Python float object.
 */
void print_python_float(PyObject *p)
{
    /* Ensure unbuffered output. */
    setbuf(stdout, NULL);

    /* Check if the object is a valid float object. */
    if (!PyFloat_Check(p)) {
        printf("Invalid Float object\n");
        return;
    }

    /* Print header information. */
    printf("[*] Python float info\n");

    /* Print object address. */
    printf("  address    : %p\n", p);

    /* Print float value. */
    printf("  value      : %f\n", ((PyFloatObject *)p)->ob_fval);
}
