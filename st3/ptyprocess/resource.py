import ctypes
import ctypes.util


class StructRLimit(ctypes.Structure):
    _fields_ = [('rlim_cur', ctypes.c_ulong), ('rlim_max', ctypes.c_ulong)]


RLIMIT_NOFILE = 8


def getrlimit(handler):
    limits = StructRLimit()
    libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
    libc.getrlimit(handler, ctypes.byref(limits))

    return (limits.rlim_cur, limits.rlim_max)
