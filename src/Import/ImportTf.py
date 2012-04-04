#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''
from Configuration.SkemaPackConfig import SkemaPackConfig
import sys
from Export.ExportFile import ExportFile
from Configuration.SkemaPackConfig import SkemaPackConfig_stdin
from Input.TfImporter.TfCsvImport import TfCsvImport
from Datatypes.EventFunctions import AdToWeeksum
from Input.DumpCsv.DumpCsvFromXml import DumpNamedSheet


def ImportTf( config = None, ConfigSet = "ImportTf" ):
    '''
    Imports events and config from file (or stdin)
    @param config: The config object to use. If None, then we try to use defaults or stdin
    @param ConfigSet: The section of the configuration to use
    @raise KeyError: If supplied ConfigSet is not in config
    @return: (weeksums, config) 
    '''  
    # filename from config
    TfFilename = config.get( ConfigSet, "Infile" )
    CsvTempFilename = config.get( ConfigSet, "CsvFile" )
    SheetName = config.get( ConfigSet, "Sheetname" )
    Separator = config.get( ConfigSet, "CsvSeparator" )

    # convert to csv
    DumpNamedSheet( TfFilename, CsvTempFilename, SheetName, Separator)

    # read csv file
    events = []
    tfi = TfCsvImport(CsvTempFilename, Separator )
    tfi.EnableImportAll()
    for Ad in tfi:
        NewEvents = AdToWeeksum( Ad )
        for e in NewEvents:
            events.append( e )
    
    return events, config


if __name__ == '__main__':

    # allow cfg file from cmd line
    if len(sys.argv) > 1:
        cfgfile = open( sys.argv[1] )
    else:
        cfgfile = SkemaPackConfig_stdin()

    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "ImportTf"

    # 3) import from skema
    Events = ImportTf( config, ConfigSet )
    
    # 4) output all events to stdout
    ExportFile( Events, config, ConfigSet )
    