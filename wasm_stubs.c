/*
 * Stub implementations for functions not available in WASM
 */

#include <Python.h>

/* Stub for raypy_loadfn - dynamic library loading not supported in WASM */
PyObject *raypy_loadfn(PyObject *self, PyObject *args) {
    PyErr_SetString(PyExc_NotImplementedError,
        "loadfn_from_file is not supported in WebAssembly environment");
    return NULL;
}
