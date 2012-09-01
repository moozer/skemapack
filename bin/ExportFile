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
            # handling utf-8 issues
            # see: http://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python
            fp = codecs.getwriter('utf8')(sys.stdout)

        # read data from file or net
        if not config.has_option(ConfigSet, "OutputDateformat"):
            DateFormat = "%Y-%m-%d"
        else:
            DateFormat = config.get(ConfigSet, "OutputDateformat")

    # outputting config first
    if config:
        fp.write( str(config).encode('utf-8') ) 
    
    try: # is this an event?
        # looping over events and outputting
        for event in Events:
            fp.write(MakeEventString(event, DateFormat ) )
    except KeyError:
        # is this a weeksum?
        for event in Events:
            ws_str = MakeWeeksumString(event, DateFormat )
            #.encode("Utf-8")
            try:
                fp.write( ws_str )
            except UnicodeDecodeError:
                sys.stderr.write( "Unicode error on line: %s"%ws_str)
            
