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

import __cfg
import __helpers
import __sync_helpers

from __helpers import __print_ok, __print_info, __print_err, _verbose

aac = None

def __aac2_init():
  # signal handlers ?

  # fscheck
  __helpers.fscheck()

  # check dependencies
  __helpers.depcheck()

def __aac2_sync():
  # init rom manifests
  __sync_helpers.initmanifests()

  # fetch rom manifests
  __sync_helpers.readmanifests()

  # list rom manifests
  __sync_helpers.rom_buffet()

  # init sync
  __sync_helpers.initsync()

def __aac2_compile():
  print ( "gee, i have to write 'compile' this yet." )
