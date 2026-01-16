"""
Python bindings for RayforceDB (WASM/Pyodide build)
"""

import sys

from rayforce.ffi import FFI

FFI.init_runtime()

version = "0.5.2"

# WASM/Pyodide: The shared library is loaded automatically by Pyodide
# when the wheel is installed, so we don't need ctypes.CDLL here
if sys.platform != "emscripten":
    # For non-WASM platforms, use the standard loading mechanism
    import ctypes
    from pathlib import Path

    if sys.platform == "linux":
        lib_name = "_rayforce_c.so"
    elif sys.platform == "darwin":
        lib_name = "_rayforce_c.so"
    elif sys.platform == "win32":
        lib_name = "rayforce.dll"
    else:
        raise ImportError(f"Platform not supported: {sys.platform}")

    lib_path = Path(__file__).resolve().parent / lib_name
    if lib_path.exists():
        try:
            ctypes.CDLL(str(lib_path), mode=ctypes.RTLD_GLOBAL)
        except Exception as e:
            raise ImportError(f"Error loading CDLL: {e}") from e


from .errors import (  # noqa: E402
    RayforceArityError,
    RayforceConversionError,
    RayforceDomainError,
    RayforceError,
    RayforceEvaluationError,
    RayforceIndexError,
    RayforceInitError,
    RayforceLengthError,
    RayforceNYIError,
    RayforceOkError,
    RayforceOSError,
    RayforceParseError,
    RayforcePartedTableError,
    RayforceQueryCompilationError,
    RayforceTCPError,
    RayforceThreadError,
    RayforceTypeError,
    RayforceTypeRegistryError,
    RayforceUserError,
    RayforceValueError,
)

# Network modules not available in WASM (no sockets)
# from .network import TCPClient, TCPServer

from .types import (  # noqa: E402
    B8,
    C8,
    F64,
    GUID,
    I16,
    I32,
    I64,
    U8,
    Column,
    Date,
    Dict,
    Expression,
    Fn,
    List,
    Null,
    Operation,
    QuotedSymbol,
    String,
    Symbol,
    Table,
    TableColumnInterval,
    Time,
    Timestamp,
    Vector,
)
from .utils import (  # noqa: E402
    eval_obj,
    eval_str,
    python_to_ray,
    ray_to_python,
)

core_version = String(eval_str("(sysinfo)")["hash"]).to_python()

__all__ = [
    "B8",
    "C8",
    "F64",
    "GUID",
    "I16",
    "I32",
    "I64",
    "U8",
    "Column",
    "Date",
    "Dict",
    "Expression",
    "Fn",
    "List",
    "Null",
    "Operation",
    "QuotedSymbol",
    "RayforceArityError",
    "RayforceConversionError",
    "RayforceDomainError",
    "RayforceError",
    "RayforceEvaluationError",
    "RayforceIndexError",
    "RayforceInitError",
    "RayforceLengthError",
    "RayforceNYIError",
    "RayforceOSError",
    "RayforceOkError",
    "RayforceParseError",
    "RayforcePartedTableError",
    "RayforceQueryCompilationError",
    "RayforceTCPError",
    "RayforceThreadError",
    "RayforceTypeError",
    "RayforceTypeRegistryError",
    "RayforceUserError",
    "RayforceValueError",
    "String",
    "Symbol",
    "Table",
    "TableColumnInterval",
    "Time",
    "Timestamp",
    "Vector",
    "core_version",
    "eval_obj",
    "eval_str",
    "python_to_ray",
    "ray_to_python",
    "version",
]
