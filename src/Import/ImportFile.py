#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''
from Datatypes.EventFunctions import WriteEvents, ReadEvent
from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin
import sys


def ImportFile( config = None, ConfigSet = "ImportFile" ):
    # if no config supplied, use defaults
    if not config:
        FileToUse = sys.stdin
        DateFormat = "%Y-%m-%d"
    else:
        # read data from file or net
        if not config.has_option(ConfigSet, "Infile"):
            FileToUse = sys.stdin
        else:
            FileToUse = open( config.get(ConfigSet, "Infile") )

        # read data from file or net
        if not config.has_option(ConfigSet, "Infile"):
            DateFormat = "%Y-%m-%d"
        else:
            DateFormat = config.get(ConfigSet, "InputDateformat")

    sys.stderr.write( "ImportFile : using %s for input\n"%FileToUse.name)

    Events = []
    for EventText in FileToUse:
        event = ReadEvent(EventText, DateFormat )
        if not event:
            continue
        
        Events.append( event )

    return Events 


if __name__ == '__main__':

    if len(sys.argv) > 2:
        config = SkemaPackConfig( sys.argv[1] )
    else:
        config = None
        
    sys.stderr.write( "ImportFile : config file is %s\n"%cfgfile)

#    # 1) read config/parameter
    ConfigSet = "SkemaScraper"

    # 3) import from skema
    Events = ImportFile( config, ConfigSet )
    
    # 4) output all events to stdout
    print config # placed here to allow config to be changed...
    WriteEvents( Events, config, ConfigSet )