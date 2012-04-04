#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''
from Datatypes.EventFunctions import ReadString
from Configuration.SkemaPackConfig import SkemaPackConfig, SkemaPackConfig_stdin_eal
import sys
from Export.ExportFile import ExportFile

def ImportFile( config = None, ConfigSet = "ImportFile" ):
    '''
    Imports events and config from file (or stdin)
    @param config: The config object to use. If None, then we try to use defaults or stdin
    @param ConfigSet: The section of the configuration to use
    @raise KeyError: If supplied ConfigSet is not in config
    @return: (events, config) or (weeksums, config) 
    '''  
    # if no config supplied, use stdin
    if not config:
        # create new config object
        config = SkemaPackConfig( SkemaPackConfig_stdin_eal() )
        # we accept non-existent section when piping from stdin
    else: 
        # check if specified section is present
        if not config.has_section( ConfigSet ):
            raise KeyError("Section \"%s\" not found"%ConfigSet)
            
      
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

    try:
        # read events
        Events = []
        for EventText in FileToUse:
            event = ReadString(EventText, DateFormat )
            if not event:
                continue
            
            Events.append( event )
    
        ret = Events 
    except KeyError:
        # read weeksums
        ws = []
        for WsText in FileToUse:
            event = ReadString(WsText, DateFormat )
            if not event:
                continue
            
            ws.append( event )
    
        ret =  ws 
        
    return (ret, config)

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
