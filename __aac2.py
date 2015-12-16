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

import argparse

import __cfg
import __helpers

from __helpers import __print_ok, __print_info, __print_err, _verbose

aac = None

def __aac2_init():
  # fscheck
  __helpers.fscheck()

  # check dependencies
  __helpers.depcheck()

def __aac2_run():
  print ( "gee, i have to write this yet." )

if (__name__ == "__main__"):
  parser = argparse.ArgumentParser()

  parser.add_argument("action", help="action", nargs="?", choices=["init", "run"])

  parser.add_argument("-v", "--verbose", help="be more verbose", action="store_true")

  args = parser.parse_args()

  if args.verbose:
    __cfg.__verbose = True

  if args.action in [None, "init"]:
    __aac2_init()
  elif args.action == "run":
    __aac2_run()
  else:
    __print_err ("something went wrong.")