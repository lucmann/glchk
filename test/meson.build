glut_dep = dependency('glut')

getString = executable(
    'getString',
    'getString.c',
    link_with : [gl_check_lib],
    dependencies : [glut_dep],
)

test('getString', getString)
