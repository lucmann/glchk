gl_check_lib_files = files(
    'glchk.c',
    'glchk.h',
    'gldl.c',
    'gldl.h',
)

gl_check_lib = shared_library(
    'glchk',
    [gl_check_lib_files],
    dependencies : [dep_dl],
    install : true,
)
