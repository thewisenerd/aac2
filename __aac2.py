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

from tkinter import *

import __cfg
import __helpers

from __helpers import __print_ok, __print_info, __print_err

aac = None

def __gui_init():
  __print_info("initializing gui... ")
  aac = Tk(None, None, __helpers.getprogramtitle(), 1, 0, None)
  aac.minsize(width=400, height=440)
  aac.maxsize(width=400, height=440)
  aac.tk_setPalette("background", "white")
  __print_ok("done\n")
  aac.mainloop()

def __aac2():
  __print_ok (__helpers.getprogramtitle() + "\n")

  # parse cmdline
  __helpers.cmdlineparse()

  # fscheck
  __helpers.fscheck()

  # gui init
  __gui_init()

if (__name__ == "__main__"):
  __aac2()