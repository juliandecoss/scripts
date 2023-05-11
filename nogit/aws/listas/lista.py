import ctypes

def magic_get_dict(o):
    # find address of dict whose offset is stored in the type
    dict_addr = id(o) + type(o).__dictoffset__
    # retrieve the dict object itself
    dict_ptr = ctypes.cast(dict_addr, ctypes.POINTER(ctypes.py_object))
    return dict_ptr.contents.value

def magic_flush_mro_cache():
    ctypes.PyDLL(None).PyType_Modified(ctypes.cast(id(object), ctypes.py_object))

print(list.__setitem__)
dct = magic_get_dict(list)
dct['__setitem__'] = lambda s, k, v: s
magic_flush_mro_cache()
print(list.__setitem__)

x = [1,2,3,4,5]
print(x.__setitem__)
x.__setitem__(0,10)
x[1] = 20
print(x)