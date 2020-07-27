
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
 * \\file gl_dl.c
 * Constructor and Destructor of the Library
 */
 

#include <dlfcn.h>
#include <GL/gl.h>
#include <stdio.h>
#include <stdlib.h>
#include "glapitable.h"

/** Globals */
static void * gl_lib_handle;
struct _glapi_table * _tbl;

static void _init( void ) __attribute__((constructor));
static void _init( void )
{
   gl_lib_handle = dlopen("libGL.so", RTLD_LOCAL | RTLD_LAZY);

   if (!gl_lib_handle)
   {
      printf("%s\\n", dlerror());
      exit(1);
   }

"""

footer = """
}

static void _fini( void ) __attribute__((destructor));
static void _fini( void )
{
   int eret;

   eret = dlclose(gl_lib_handle);

   if (eret)
   {
      printf("%s\\n", dlerror());
   }
}
"""

class PrintDl(gl_XML.gl_print_base):
    def __init__(self):
        gl_XML.gl_print_base.__init__(self)

        self.undef_list.append( "NAME" )
        self.name = "gl_dl.py (from Mesa)"

    def printBody(self, api):
        for f in api.functionIterateByOffset():
            print('   ((glapi_func *) _tbl)[%4d] = dlsym(gl_lib_handle, "NAME(%s)");' % (
                f.offset, f.name))

    def printRealHeader(self):
        print(header)

    def printRealFooter(self):
        print(footer)


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

    PrintDl().Print(api)


if __name__ == '__main__':
    main()
