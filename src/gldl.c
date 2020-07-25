//
// Created by luc on 2020/7/25.
//

#include <stdio.h>
#include <stdlib.h>
#include "glchk.h"
#include "gldl.h"

static void * gl_so;
GetString _glchk_GetString;

static void _init( void ) __attribute__((constructor));
static void _init( void )
{
   gl_so = dlopen("libGL.so", RTLD_LOCAL | RTLD_LAZY);

   if (!gl_so)
   {
      printf("%s\n", dlerror());
      exit(1);
   }

   _glchk_GetString = (GetString)dlsym(gl_so, "glGetString");
}

static void _fini( void ) __attribute__((destructor));
static void _fini( void )
{
   int eret;

   eret = dlclose(gl_so);

   if (eret)
   {
      printf("%s\n", dlerror());
   }
}
