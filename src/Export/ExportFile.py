#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''

from Datatypes.EventFunctions import WriteEvents, ReadEvent, MakeEventString
from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin
import sys

   
def ExportFile( Events, config, ConfigSet = "ExportFile" ):
    # read data from file or net
    fp = open(config.get(ConfigSet, "Outfile"), 'w')

    for event in Events:
        fp.write(MakeEventString(event, config.get(ConfigSet, "OutputDateformat")) )

    fp.close()
    return

#if __name__ == '__main__':
#
#    if len(sys.argv) > 2:
#        cfgfile = sys.argv[1]
#    else:
#        cfgfile = SkemaPackConfig_stdin()
#
##    # 1) read config/parameter
#    config = SkemaPackConfig( cfgfile )
#    ConfigSet = "SkemaScraper"
#
#    # 3) import from skema
#    Events = ImportFile( config, ConfigSet )
#    
#    # 4) output all events to stdout
#    print config # placed here to allow config to be changed...
#    WriteEvents( Events, config, ConfigSet )
