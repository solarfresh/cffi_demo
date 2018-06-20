from cffi import FFI

ffi = FFI()
ffi.cdef("""
    typedef struct { int x, y; } point_t;
    int do_stuff(point_t *);
""")
C = ffi.dlopen("plugin-1.5.dll")
arg = ffi.new("point_t[]", [(3, 4)])

print(C.do_stuff(arg))
