#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Dec 29, 2011

@author: morten
'''

import sys
from Output.IcsOutput.IcsOutput import IcsOutput
from Configuration.SkemaPackConfig import SkemaPackConfig, SkemaPackConfig_stdin_eal
from Import.ImportFile import ImportFile

def ExportIcs( Events, config, ConfigSet = "ExportIcs" ):
    ''' Configuration items needed are the same as for ReadEvent() 
        and 'OutputFile', 'InputFile'
    @param Events: the events to output 
    @param Config: the configuration object to use
    @param ConfigSet: The sub set of the configuration object.
    '''
        
    io = IcsOutput( Events )

    # save to file or stdout as specified in the config.
    outfile = config.get( ConfigSet, 'OutFile' )

    f = open( outfile, "wb" )
    f.write( io.GetIcsString() )
    f.close()
    
if __name__ == '__main__':
    # allow cfg file from cmd line
    if len(sys.argv) > 1:
        cfgfile = open( sys.argv[1] )
    else:
        cfgfile = SkemaPackConfig_stdin_eal()

    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "ExportIcs"

    # 3) import from file (which might be stdin
    Events = ImportFile( config, ConfigSet )
    
    # 4) output all events to ics
    ExportIcs( Events, config )
    
    