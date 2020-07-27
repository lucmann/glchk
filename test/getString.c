//
// Created by luc on 2020/7/25.
//
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <GL/gl.h>
#include <GLFW/glfw3.h>

int main(int argc, char **argv)
{
   char *vendor;

   /** Context Initialization */
   glfwInitHint(GLFW_COCOA_MENUBAR, GLFW_FALSE);

   if (!glfwInit())
      exit(EXIT_FAILURE);

   glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
   GLFWwindow *os_win = glfwCreateWindow(640, 480, "", NULL, NULL);
   if (!os_win)
   {
      glfwTerminate();
      exit(EXIT_FAILURE);
   }

   glfwMakeContextCurrent(os_win);

   vendor = glGetString(GL_VENDOR);

   assert(vendor);

   printf("%s\n", vendor);

   return 0;
}
