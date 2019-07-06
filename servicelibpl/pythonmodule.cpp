#include "servicelibpl.h"


static PyMethodDef servicelibplMethods[] =
{
	 {NULL,NULL,0,NULL}
};

PyMODINIT_FUNC
initservicelibpl(void)
{
	Py_InitModule("servicelibpl", servicelibplMethods);
}
