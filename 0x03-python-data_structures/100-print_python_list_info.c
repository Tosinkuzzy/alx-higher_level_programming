#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
int size = PyList_Size(p);
int alloc = ((PyListObject *)p)->allocated;
int i;

printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (i = 0; i < size; i++)
{
printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
}
