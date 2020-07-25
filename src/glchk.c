//
// Created by luc on 2020/7/25.
//

#include "glchk.h"

extern GetString _glchk_GetString;

GLAPI const GLubyte * GLAPIENTRY glGetString( GLenum name )
{
   return _glchk_GetString(GL_VENDOR);
}
