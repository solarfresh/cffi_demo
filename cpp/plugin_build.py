# file plugin_build.py
import cffi
ffibuilder = cffi.FFI()

with open('plugin.h') as f:
    # read plugin.h and pass it to embedding_api(), manually
    # removing the '#' directives and the CFFI_DLLEXPORT
    data = ''.join([line for line in f if not line.startswith('#')])
    data = data.replace('CFFI_DLLEXPORT', '')
    ffibuilder.embedding_api(data)

ffibuilder.set_source("my_plugin", r'''
    #include "plugin.h"
''')

ffibuilder.embedding_init_code("""
    from my_plugin import ffi

    @ffi.def_extern()
    def do_stuff(p):
        print("adding %d and %d" % (p.x, p.y))
        return p.x + p.y
""")

ffibuilder.compile(target="plugin-1.5.*", verbose=True)
# or: ffibuilder.emit_c_code("my_plugin.c")
