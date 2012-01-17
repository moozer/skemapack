'''
Created on Sep 16, 2011

@author: flindt
'''
from Configuration.SkemaPackConfig import SkemaPackConfig
from optparse import OptionParser

import sys

def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-c", "--configfile", dest="ConfigFileName",
                      help="Load configuration from this file")
   
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options

def ReadOptions( Silent = False ):
    opt = ParseCmdLineOptions()
    
    if not Silent:
        print "## commandLine options:"
        print "## %s" % opt
    
    try:
        config = SkemaPackConfig(opt.ConfigFileName)
    except:
        print "No configuration file found. Try 'ImportSdeSkema.py --configfile=myconfig.cfg'"
        sys.exit(1)  

    return config

