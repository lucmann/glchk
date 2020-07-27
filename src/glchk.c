//
// Created by luc on 2020/7/25.
//

#include <GL/gl.h>
#include "glapitable.h"

extern struct _glapi_table * _tbl;

GLAPI const GLubyte * GLAPIENTRY glGetString( GLenum name )
{
   glapi_func _func = ((glapi_func *) _tbl)[275];

   return ((const GLubyte * (APIENTRY *)(GLenum name)) _func)(name);
}
