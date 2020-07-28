subdir('gen')

gl_check_lib = shared_library(
    'glchk',
    [gl_check_c, gl_dl_c, glapitable_h],
    dependencies : [dep_dl],
    install : true,
)
