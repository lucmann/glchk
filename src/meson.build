subdir('gen')

gl_check_lib_files = files(
    'glchk.c',
    'glchk.h',
)

gl_check_lib = shared_library(
    'glchk',
    [gl_check_lib_files, gl_dl_c, glapitable_h],
    dependencies : [dep_dl],
    install : true,
)
