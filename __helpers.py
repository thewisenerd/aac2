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

import shutil
import stat
import subprocess
import sys
import os

from inspect import getsourcefile

import __cfg

def _aac2_dir():
  return os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))

def _verbose():
  return __cfg.__verbose

def which(program):
  def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

  fpath, fname = os.path.split(program)
  if fpath:
    if is_exe(program):
      return program
  else:
    for path in os.environ["PATH"].split(os.pathsep):
      path = path.strip('"')
      exe_file = os.path.join(path, program)
      if is_exe(exe_file):
        return exe_file

  return None

def fscheck():
  __print_info("checking fs:\n")

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

def depcheck():
  __print_info("checking dependencies:" + "\n")
  __print_info("  getting root... ")
  sys.stdout.flush()
  # gksudo ?
  cmd = ['sudo', 'python3', _aac2_dir() + '/__install_dependencies.py']
  ret = subprocess.call(cmd)
  if ret != 0:
    quit()

  # install repo
  __print_info("  installing repo:" + "\n")

  __print_info("    checking previous install... ")
  sys.stdout.flush()

  if which("repo") is None:
    __print_err("fail" + "\n")
    sys.stdout.flush()

    # new install repo
    __print_info("    installing repo... ")

    try:
      shutil.copyfile((_aac2_dir() + '/binaries/repo'), (os.environ['HOME'] + '/bin/repo'))
    except Exception as arg:
      __print_err("fail" + "\n")
      sys.stdout.flush()
      exit(-1)
    __print_ok ("ok" + "\n")
  else:
    __print_ok("ok" + "\n")

  # chmod/chown repo
  st = os.stat((os.environ['HOME'] + '/bin/repo'))
  os.chmod((os.environ['HOME'] + '/bin/repo'), st.st_mode | stat.S_IEXEC)

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