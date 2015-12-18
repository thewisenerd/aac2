#!/usr/bin/env python3

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

import os
import sys

import time

try:
  import apt
except Exception as arg:
  __print_err("fail" + "\n")
  exit(-1)

def __print_ok(_str):
  print ('\033[32m' + _str + '\033[39m', end='')

def __print_info(_str):
  print ('\033[33m' + _str + '\033[39m', end='')

def __print_err(_str):
  print ('\033[31m' + _str + '\033[39m', end='')

def last_apt_update():
  return ( time.time() - os.path.getmtime('/var/cache/apt/pkgcache.bin') )

def check_root():
  euid = os.geteuid()
  if euid != 0:
    __print_err("fail" + "\n")
    exit(-1)

  # get back to main prog 'getting root... '
  __print_ok ("ok" + "\n")

def __install_deps():
  __print_info ("  running apt-get update... ")
  sys.stdout.flush()

  cache = apt.cache.Cache()

  # last apt-get update was run less than 30 minutes ago = skip
  if (last_apt_update() < (30 * 60) ):
    __print_ok("ok" + "\n")
  else:
    try:
      cache.update()
    except Exception as arg:
      __print_err("fail" + "\n")
      exit(-1)
    __print_ok("ok" + "\n")

  # re-open cache
  cache.open(None)

  __print_info ("  installing packages:" + "\n")

  # - lib32z-dev
  # + lib32z1-dev
  #
  # + openjdk-7-jdk
  # + openjdk-7-jre
  #
  # + bc
  deps = [
    "git-core", "gnupg", "flex", "bison", "gperf", "build-essential", "zip",
    "curl", "zlib1g-dev", "gcc-multilib", "g++-multilib", "libc6-dev-i386",
    "lib32ncurses5-dev", "x11proto-core-dev", "libx11-dev", "lib32z1-dev",
    "ccache", "libgl1-mesa-dev", "libxml2-utils", "xsltproc", "unzip",
    "openjdk-7-jdk", "openjdk-7-jre", "bc"
  ]

  for pkg_name in deps:
    pkg = cache[pkg_name]
    __print_info ( "    {pkg_name}... ".format(pkg_name=pkg_name) )
    sys.stdout.flush()
    if pkg.is_installed:
      __print_ok ( "ok" + "\n")
    else:
      pkg.mark_install()
      try:
        cache.commit()
      except Exception as arg:
        __print_err("fail" + "\n")
        exit(-1)
      __print_ok ( "ok" + "\n")

def app():
  check_root()

  __install_deps()

if (__name__ == "__main__"):
  app()
