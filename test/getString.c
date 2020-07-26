//
// Created by luc on 2020/7/25.
//
#include <assert.h>
#include <stdio.h>
#include <GL/gl.h>
#include <GLFW/glfw3.h>

int main(int argc, char **argv)
{
   char *vendor;

   /** Context Initialization */
   glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
   GLFWwindow *os_ctx = glfwCreateWindow(640, 480, "", NULL, NULL);
   glfwMakeContextCurrent(os_ctx);

   vendor = glGetString(GL_VENDOR);

   assert(vendor);

   printf("%s\n", vendor);

   return 0;
}
