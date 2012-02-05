#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''
from Datatypes.EventFunctions import WriteEvents, ReadEvent
from Configuration.SkemaPackConfig import SkemaPackConfig
import sys
from Export.ExportFile import ExportFile

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
        if not config.has_option(ConfigSet, "InputDateformat"):
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
    # initial vars
    Module = "ImportFile"
    ConfigSet = "SkemaScraper"
    
    # handle command line config file (if set)
    if len(sys.argv) > 2:
        config = SkemaPackConfig( sys.argv[1] )
        sys.stderr.write( "%s : config file is %s\n"%(Module, config.name))
    else:
        config = None
        sys.stderr.write( "%s : config from stdin\n"%Module)
        
    # import from file
    Events = ImportFile( config, ConfigSet )
    
    # output to file
    ExportFile( Events, config, ConfigSet )
