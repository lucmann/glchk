
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


class PrintGlTable(gl_XML.gl_print_base):
    def __init__(self):
        gl_XML.gl_print_base.__init__(self)

        self.header_tag = '_GLAPI_TABLE_H_'
        self.name = "gl_table.py (from Mesa)"

    def printBody(self, api):
        for f in api.functionIterateByOffset():
            arg_string = f.get_parameter_string()
            print('   %s (GLAPIENTRYP %s)(%s); /* %d */' % (
                f.return_type, f.name, arg_string, f.offset))

    def printRealHeader(self):
        print('#ifndef GLAPIENTRYP')
        print('# ifndef GLAPIENTRY')
        print('#  define GLAPIENTRY')
        print('# endif')
        print('')
        print('# define GLAPIENTRYP GLAPIENTRY *')
        print('#endif')
        print('')
        print('#define NAME(func)   gl##func')
        print('')
        print('#ifdef __cplusplus')
        print('extern "C" {')
        print('#endif')
        print('')
        print('typedef void (*glapi_func)(void);')
        print('')
        print('struct _glapi_table')
        print('{')
        return

    def printRealFooter(self):
        print('};')
        print('')
        print('#ifdef __cplusplus')
        print('}')
        print('#endif')
        return


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

    PrintGlTable().Print(api)


if __name__ == '__main__':
    main()
