# Copyright (c) 2015 - thewisenerd <thewisenerd@protonmail.com>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import sys
import os

import __cfg

def getprogramtitle():
  return (__cfg.__title__ + " v" + __cfg.__version__)

def cmdlineparse():
  __print_info("parsing cmdline... ")
  argv_length = len(sys.argv)
  if (argv_length == 1):
    __print_ok("done\n")
    return;
  for key,value in enumerate(sys.argv):
    if (key == 0):
      continue;
    _a = value[1:].split('=')
    if _a[0] == 'v':
      __cfg.__verbose = True
      #print ("set verbose to true")
    elif _a[0] == '-help':
      print ("see /DOCUMENTATION.txt for help")
      quit()
  __print_ok("done\n")

def fscheck():
  __print_info("checking fs... \n")

  # os check
  __print_info("  checking os... ")
  if (os.name is not 'posix'):
    __print_err("fail\n")
    quit()
  else:
    __print_ok("ok\n")

  # cwd check for spaces
  __print_info("  checking cwd... ")
  if os.getcwd().find(" ") is not -1:
    __print_err("fail\n")
    quit()
  else:
    __print_ok("ok\n")

# OS Colors
__osc = {
  'red'    : '\033[31m',
  'green'  : '\033[32m',
  'yellow' : '\033[33m',
# 'color'  : 'code',
  'end'    : '\033[39m',
}

__osc['err']  = __osc['red']
__osc['ok']   = __osc['green']
__osc['info'] = __osc['yellow']

# __print_*
def __print_ok(_str):
  print (__osc['ok'] + _str + __osc['end'], end='')

def __print_info(_str):
  print (__osc['info'] + _str + __osc['end'], end='')

def __print_err(_str):
  print (__osc['err'] + _str + __osc['end'], end='')