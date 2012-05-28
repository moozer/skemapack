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

    StartWeekText = config.get(ConfigSet, "StartWeek")
    if StartWeekText != "":
        StartWeek = [int(x) for x in StartWeekText.split("-") ]
    EndWeekText = config.get(ConfigSet, "EndWeek")
    if EndWeekText != "":
        EndWeek = [int(x) for x in EndWeekText.split("-") ]
    
    res = []
    for e in Events:
        # filter on teacher
        if Teacher != "":
            if e['Teacher'] != Teacher:
                continue

        # handling period
        if StartWeekText != "":
            if (e['Year'] < StartWeek[0]):
                continue
            if (e['Year'] == StartWeek[0]) and (e['Week'] < StartWeek[1]):
                continue
            
        if EndWeekText != "":
            if (e['Year'] > EndWeek[0]):
                continue
            if (e['Year'] == EndWeek[0]) and (e['Week'] > EndWeek[1]):
                continue
            
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