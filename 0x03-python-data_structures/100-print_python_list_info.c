#include <python.h>
#include <object.h>
#include<listobject.h>

/**
 *print_python_list_info - print info about a python list
 * @p: parameter
 * Return: Null
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		print("Element %i: %s\n", i, PY_TYPE(obj->ob_item[i])->tp_name);
}
