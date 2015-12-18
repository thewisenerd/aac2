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

import argparse
import sys

import __cfg
import __helpers

from __aac2 import __aac2_compile, __aac2_init, __aac2_sync

if (__name__ == "__main__"):
  global args

  parser = argparse.ArgumentParser()

  parser.add_argument("action", help="action", nargs="?", choices=["init", "sync", "compile"])

  parser.add_argument("-v", "--verbose", help="be more verbose", action="store_true")

  parser.add_argument("--skip-repo-check", help="stop checking for .repo", action="store_true")

  parser.add_argument("--skip-apt", help="stop packages check", action="store_true")

  args = parser.parse_args()

  if args.verbose:
    __cfg.__verbose = True

  if args.action in [None, "init"]:
    __aac2_init()
  elif args.action == "sync":
    __aac2_sync()
  elif args.action == "compile":
    __aac2_compile()
  else:
    __helpers.__print_err ("something went wrong." + "\n")
    sys.stdout.flush()
    exit(-1)

  exit()
