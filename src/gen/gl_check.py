
# (C) Copyright IBM Corporation 2004
# All Rights Reserved.
# Copyright (c) 2014 Intel Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# on the rights to use, copy, modify, merge, publish, distribute, sub
# license, and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.  IN NO EVENT SHALL
# IBM AND/OR ITS SUPPLIERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# Authors:
#    Ian Romanick <idr@us.ibm.com>

from __future__ import print_function

import argparse

import gl_XML


header = """/**
 * \\file gl_check.c
 * Wrappers of GL commands with glGetError
 */
 

#include <GL/gl.h>
#include <stdio.h>
#include <stdlib.h>
#include "glapitable.h"

extern struct _glapi_table * _tbl;
extern GetError getError; 

static void _gl_check(const char *func)
{
   GLenum err;
   
   while ((err = getError()) != GL_NO_ERROR)
   {
      char *error; 

      switch (err)
      {
      case GL_INVALID_OPERATION:             error = "INVALID_OPERATION"; break;
      case GL_INVALID_ENUM:                  error = "INVALID_ENUM"; break;
      case GL_INVALID_VALUE:                 error = "INVALID_VALUE"; break;
      case GL_OUT_OF_MEMORY:                 error = "OUT_OF_MEMORY"; break;  
      case GL_INVALID_FRAMEBUFFER_OPERATION: error = "INVALID_FRAMEBUFFER_OPERATION"; break;
      }
      
      printf("%s: %s\\n", func, error);
   }
}
"""

class PrintGlCheck(gl_XML.gl_print_base):
    def __init__(self):
        gl_XML.gl_print_base.__init__(self)

        self.undef_list.append( "NAME" )
        self.name = "gl_check.py (from Mesa)"

    def printBody(self, api):
        for f in api.functionIterateByOffset():
            if f.return_type != 'void':
                self.printFunctionWithReturn(f)
            else:
                self.printFunctionNoReturn(f)

    def printRealHeader(self):
        print(header)

    def printRealFooter(self):
        print('')

    def _c_cast(self, f):
        cast = '%s (GLAPIENTRY *)(%s)' % (f.return_type, f.get_parameter_string())

        return cast

    def printFunctionWithReturn(self, f):
        print('')
        print('GLAPI %s GLAPIENTRY NAME(%s)(%s)' % (f.return_type, f.name, f.get_parameter_string()))
        print('{')
        print('   %s retval;' % f.return_type)
        print('')
        print('   glapi_func _func = ((glapi_func *) _tbl)[%d];' % f.offset)
        print('   retval = ((%s) _func)(%s);' % (self._c_cast(f), f.get_called_parameter_string()))
        print('')
        print('   _gl_check(__func__);')
        print('')
        print('   return retval;')
        print('}')
        print('')

    def printFunctionNoReturn(self, f):
        print('')
        print('GLAPI %s GLAPIENTRY NAME(%s)(%s)' % (f.return_type, f.name, f.get_parameter_string()))
        print('{')
        print('   glapi_func _func = ((glapi_func *) _tbl)[%d];' % f.offset)
        print('')
        print('   ((%s) _func)(%s);' % (self._c_cast(f), f.get_called_parameter_string()))
        print('')
        print('   _gl_check(__func__);')
        print('}')
        print('')


def _parser():
    """Parse arguments and return a namespace."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename',
                        default='gl_API.xml',
                        metavar="input_file_name",
                        dest='file_name',
                        help="Path to an XML description of OpenGL API.")
    return parser.parse_args()


def main():
    """Main function."""
    args = _parser()

    api = gl_XML.parse_GL_API(args.file_name)

    PrintGlCheck().Print(api)


if __name__ == '__main__':
    main()
