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
import subprocess

import json

import __cfg
import __helpers
import __main__

from __helpers import __print_err, __print_info, __print_ok, _aac2_dir

_roms = []
romchoix = None
branchchoix = None

def getmanifestsfolder():
  # add support for setting manifests folder
  return os.path.dirname(_aac2_dir()) + '/' + __cfg.__rom_manifests_folder

def _list_valid_manifests():
  return [x for x in os.listdir(getmanifestsfolder()) if x.endswith(".manifest.json")]

def initmanifests():
  __print_info("checking manifests dir... ")

  if os.path.isdir(getmanifestsfolder()):
    if len(_list_valid_manifests()):
      __print_ok ( "ok" + "\n" )
    else:
      __print_err ( "fail" + "\n" )
      sys.stdout.flush()
      exit(-1)
  else:
    __print_err ( "fail" + "\n" )
    sys.stdout.flush()
    exit(-1)

def checkmanifestdata(data):
  if (data['name'] == None):
    return False

  if (data['manifest'] == None):
    return False

  if (len(data['branches']) == 0):
    return False

  for x in data['branches']:
    if x['name'] == None:
      return False

  return True

def readmanifests():
  global _roms

  __print_info ("reading manifests:" + "\n")

  for manifest in _list_valid_manifests():
    __print_info ("  " + manifest.replace(".manifest.json", "") + "... ")
    with open( getmanifestsfolder() + manifest ) as f:
      try:
        data = json.load(f)
        if checkmanifestdata(data):
          _roms.append(data)
          __print_ok("ok" + "\n")
        else:
          __print_err("fail" + "\n")
      except Exception as arg:
        __print_err("fail" + "\n")

  if (len(_roms) == 0):
    exit(-1)

def startsync():
  syncjobs = 4
  inp = input ( __helpers.__osc['info'] + ( "sync jobs[%d]: " % (syncjobs) ) + __helpers.__osc['end'] )
  if inp != "":
    try:
      syncjobs = int(inp)
    except Exception as arg:
      syncjobs = 4
      pass

  cmd = "repo sync -j%d" % syncjobs

  __print_info("starting sync: " + "\n")
  ret = subprocess.call(cmd, shell=True)

  if ret == 0:
    __print_ok ("ok" + "\n")
  else:
    __print_err("fail" + "\n")
    exit(-1)

def repocheck():
  if (__main__.args.skip_repo_check) != True:
    __print_info("check .repo: ")
    sys.stdout.flush()
    if (os.path.isdir('.repo')):
      __print_err("fail" + "\n")
      __print_info("it is possible you already have repo init.\n")

      inp = input ( __helpers.__osc['info'] + ( "do you want to continue (yes/no) [no]: " ) + __helpers.__osc['end'] )
      if inp in ["y", "yes"]:
        startsync()
        exit(0)
      else:
        exit(-1)
    else:
      __print_ok("ok" + "\n")

def rom_buffet():
  global _roms
  global romchoix
  global branchchoix

  __print_info ( "-----------------" + "\n" )
  __print_info ( "||ROM Selection||" + "\n" )
  __print_info ( "-----------------" + "\n" )

  for [key, rom] in enumerate(_roms):
    __print_info ( "%02d. %s\n" %  ((key+1), rom['name']) )
  # get a while loop going here; till valid values are got
  inp = input ( __helpers.__osc['info'] + ( "select %02d-%02d [%02d]: " % (1, len(_roms), 1) ) + __helpers.__osc['end'] )
  if inp == "":
    romchoix = 0
  else:
    romchoix = int(inp)
    if ((romchoix > 0) and romchoix <= len(_roms)):
      romchoix = romchoix - 1
    else:
      romchoix = 0
  __print_info ( "-----------------" + "\n" )

  # branch selection

  __print_info ( "--------------------" + "\n" )
  __print_info ( "||Branch Selection||" + "\n" )
  __print_info ( "--------------------" + "\n" )

  for [key, branch] in enumerate(_roms[romchoix]['branches']):
    __print_info ( "%02d. %s\n" %  ((key+1), branch['name']) )
  # get a while loop going here; till valid values are got
  inp = input ( __helpers.__osc['info'] + ( "select %02d-%02d [%02d]: " % (1, len(_roms[romchoix]['branches']), 1) ) + __helpers.__osc['end'] )
  if inp == "":
    branchchoix = 0
  else:
    branchchoix = int(inp)
    if ((branchchoix > 0) and branchchoix <= len(_roms[romchoix]['branches'])):
      branchchoix = branchchoix - 1
    else:
      branchchoix = 0
  __print_info ( "-----------------" + "\n" )

  __print_info ( "choice: %s (%s)\n" % (_roms[romchoix]['name'], _roms[romchoix]['branches'][branchchoix]['name']) )
  __print_info ( "-----------------" + "\n" )

def initsync():
  __print_info("initializing sync:" + "\n")

  ref = None
  inp = input ( __helpers.__osc['info'] + ( "reference path [none]: " ) + __helpers.__osc['end'] )
  if inp != "":
    ref = inp

  if ref != None:
    if os.path.isdir(ref):
      ref = " --reference=" + ref
    else:
      ref = ""
  else:
    ref = ""

  cmd = "repo init %s -u %s -b %s" % (ref, _roms[romchoix]['manifest'], _roms[romchoix]['branches'][branchchoix]['name'])

  ret = subprocess.call(cmd, shell=True)

  __print_info("repo init... ")
  sys.stdout.flush()

  if ret == 0:
    __print_ok ("ok" + "\n")
  else:
    __print_err("fail" + "\n")
    exit(-1)

  startsync()
