#!/usr/bin/python2.6 -tt

# to run standalone on lxplus one must use python 2.6 because there is no other standalone python installation

import sys
import os
import json
import subprocess
import re
import glob

from datetime import datetime

# https://docs.python.org/2/library/optparse.html
#from optparse import OptionParser

sys.path.append( "lib" )
from utils import MyOptionParser
from utils import TextColor
from utils import get_list_of_files
from analyzers import SimAnalyzer

# ___________________________________________________________________________________


def main():

   # options from command line
   optmgr = MyOptionParser()
   if not optmgr.opt_status() :
      return 0
      
   options, _ = optmgr.get_opt() # tuple, unpack the return value and assign it the variable named to the left; _ single value to unpack
   
   print TextColor.EXEC
   
   # get list of files
   files = get_list_of_files( options.input )
   
   max_events = options.max_events
   pileup = options.pileup
   bx = options.bx
   nscans = options.vdm_points
   output = options.output_file
   beamsw = options.beams_width
   
   analysis = SimAnalyzer(files,maxEvents=max_events)
   analysis.set_pileup(pileup)
   analysis.set_bx(bx)
   analysis.set_vdm(nscans)
   analysis.set_output_file(output)
#   analysis.set_bx_space(bx_space)

   analysis.analyze()
   
# ___________________________________________________________________________________

if __name__ == '__main__':
   main()

print TextColor.ENDC
