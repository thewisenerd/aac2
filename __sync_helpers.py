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

import __cfg

from __helpers import __print_err, __print_info, __print_ok, _aac2_dir

def getmanifestsfolder():
  # add support for setting manifests folder
  return _aac2_dir() + '/' + __cfg.__rom_manifests_folder

def initmanifests():
  __print_info("checking manifests dir... ")

  if os.path.isdir(getmanifestsfolder()):
    if len([x for x in os.listdir(getmanifestsfolder()) if x.endswith(".manifest.json")]):
      __print_ok ( "ok" + "\n" )
    else:
      __print_err ( "fail" + "\n" )
      sys.stdout.flush()
      exit(-1)
  else:
    __print_err ( "fail" + "\n" )
    sys.stdout.flush()
    exit(-1)
