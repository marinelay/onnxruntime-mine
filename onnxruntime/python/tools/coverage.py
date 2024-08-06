import onnxruntime
import ctypes

_LIB = ctypes.CDLL(onnxruntime.__file__.replace(
    '__init__.py', 'capi/onnxruntime_pybind11_state.so'))

# calling `reset`, the coverage will not be ZERO (but very small, e.g., 6).
reset = _LIB.mcov_reset

push = _LIB.mcov_push_coverage
pop = _LIB.mcov_pop_coverage

get_total = _LIB.mcov_get_total
get_now = _LIB.mcov_get_now

set_now = _LIB.mcov_set_now

_char_array = ctypes.c_char * get_total()


def get_hitmap():
    hitmap_buffer = bytearray(get_total())
    _LIB.mcov_copy_hitmap(_char_array.from_buffer(hitmap_buffer))
    return hitmap_buffer


def set_hitmap(data):
    assert len(data) == get_total()
    _LIB.mcov_set_hitmap(_char_array.from_buffer(data))