#include "orbit_mpi.hh"

#include "wrap_tracker3dfield.hh"
#include "wrap_runge_kutta_tracker.hh"

static PyMethodDef tracker3dfieldMethods[] = { {NULL,NULL} };

#ifdef __cplusplus
extern "C" {
#endif

  void inittracker3dfield(){
    //create new module
    PyObject* module = Py_InitModule("tracker3dfield",tracker3dfieldMethods);
		//add the other classes init
		wrap_tracker3dfield::initRungeKuttaTracker(module);
  }
	
#ifdef __cplusplus
}
#endif

