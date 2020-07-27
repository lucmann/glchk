project(
    'glchk',
    ['c'],
    default_options : ['c_std=c99'],
)

prog_python = import('python').find_installation('python3')

cc = meson.get_compiler('c')

null_dep = dependency('', required : false)

dep_dl = null_dep
if not cc.has_function('dlopen')
    dep_dl = cc.find_library('dl', required : true)
endif

subdir('src')
subdir('test')
