glfw_dep = dependency('glfw3')

getString = executable(
    'getString',
    'getString.c',
    link_with : [gl_check_lib],
    dependencies : [glfw_dep],
)

test('getString', getString)
