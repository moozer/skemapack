#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''

from Datatypes.EventFunctions import MakeEventString, MakeWeeksumString
#from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin
import sys
import codecs

   
def ExportFile( Events, config = None, ConfigSet = "ExportFile" ):
    # read data from file or net
    if not config:
        fp = sys.stdout
        DateFormat = "%Y-%m-%d"
    else:
        # get output file name
        if config.has_option(ConfigSet, "Outfile"):
            fp = codecs.open(config.get(ConfigSet, "Outfile"), 'w', 'utf-8')
        else:
            fp = sys.stdout

        # read data from file or net
        if not config.has_option(ConfigSet, "OutputDateformat"):
            DateFormat = "%Y-%m-%d"
        else:
            DateFormat = config.get(ConfigSet, "OutputDateformat")

    # outputting config first
    if config:
        fp.write( str(config) ) 
    
    try: # is this an event?
        # looping over events and outputting
        for event in Events:
            fp.write(MakeEventString(event, DateFormat ) )
    except KeyError:
        # is this a weeksum?
        for event in Events:
            ws_str = MakeWeeksumString(event, DateFormat )
            fp.write( ws_str )
    




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
