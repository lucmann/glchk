//
// Created by luc on 2020/7/25.
//
#include <assert.h>
#include <stdio.h>
#include <GL/gl.h>
#include <GL/glut.h>

int main(int argc, char **argv)
{
   char *vendor;

   vendor = glGetString(GL_VENDOR);

   assert(vendor);

   printf("%s\n", vendor);

   return 0;
}
