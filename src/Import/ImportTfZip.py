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
from zipfile import ZipFile
from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin


def ImportTfZip( config = None, ConfigSet = "ImportFile" ):
    '''
    Imports events and config from file (or stdin)
    @param config: The config object to use. If None, then we try to use defaults or stdin
    @param ConfigSet: The section of the configuration to use
    @raise KeyError: If supplied ConfigSet is not in config
    @return: (weeksums, config) 
    '''  

    # fetch config values
    ZipDataDir = config.get( ConfigSet, "ZipDataDir" )
    ZipFilename = config.get( ConfigSet, "ZipFile" )

    zf = ZipFile( ZipFilename )
    zf.extractall( ZipDataDir )

    ImportTfSection = "ImportTf" 
    for DataFile in zf.namelist():    
        config.set( ImportTfSection, "Infile", DataFile )
        print "%s"%config
    
    return [], config


if __name__ == '__main__':

    # allow cfg file from cmd line
    if len(sys.argv) > 1:
        cfgfile = open( sys.argv[1] )
    else:
        cfgfile = SkemaPackConfig_stdin()

    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "ImportTfZip"

    # 3) import from skema
    Events = ImportTfZip( config, ConfigSet )
    
    # 4) output all events to stdout
    ExportFile( Events, config, ConfigSet )
    