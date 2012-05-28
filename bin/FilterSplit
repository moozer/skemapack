#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 26 May 2012

@author: moz
'''
from Configuration.SkemaPackConfig import SkemaPackConfig
import sys
from Import.ImportFile import ImportFile
from Export.ExportFile import ExportFile

def FilterSplit( Events, config = None, ConfigSet="FilterSplit" ):
    
    Teacher = config.get(ConfigSet, "Teacher")
    
    res = []
    for e in Events:
        if e['Teacher'] == Teacher:
            res.append(e)
            
    return res, config


if __name__ == '__main__':
        # initial vars
    Module = "FilterSplit"
    ConfigSet = "FilterSplit"
    
    # handle command line config file (if set)
    if len(sys.argv) > 2:
        config = SkemaPackConfig( sys.argv[1] )
    else:
        config = None
        
    # import from file
    Events, config = ImportFile( config, ConfigSet )
    
    Ws, config = FilterSplit( Events, config, ConfigSet )
    
    # output to file
    ExportFile( Ws, config, ConfigSet )