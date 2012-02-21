#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 7 Feb 2012

@author: moz
'''
from Import.ImportFile import ImportFile
from Export.ExportFile import ExportFile
from Configuration.SkemaPackConfig import SkemaPackConfig
import sys

def ConvertToWeeksum( events, config, ConfigSet = "ConvertToWeeksum"):
    
    Weeksum = {}
    WeekData = {}
    
    # loop over all events and do the sum.    
    for event in events:
        Year, Week, Weekday = event['Date'].isocalendar() #@UnusedVariable
        
        key = "%d-%d-%s-%s-%s"%(Year, Week, event['Subject'], event['Class'], event['Teacher'])
        if not key in Weeksum.keys():
            Weeksum[key] = 0
            WeekData[key] = event # all subsequent data sets are the same
            
        Weeksum[key] += 1

    # and convert to nice iterable list (sorted by year, week, subject, etc)
    Result = []
    for key in sorted( Weeksum.keys()):
        Year, Week, Weekday = WeekData[key]['Date'].isocalendar() #@UnusedVariable
        entry = { 'Year': Year, 'Week': Week, 
                  'Subject': WeekData[key]['Subject'], 'Class': WeekData[key]['Class'],
                  'LessonCount': Weeksum[key], 'Teacher': WeekData[key]['Teacher']}
        Result.append(entry)

    return Result

if __name__ == '__main__':
        # initial vars
    Module = "ConvertToWeeksum"
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
    
    Ws = ConvertToWeeksum( Events, config, ConfigSet )
    print config # placed here to allow config to be changed...

    # output to file
    # TODO: this breaks since ExportFile doesn'tknow about week sums.
    ExportFile( Ws, config, ConfigSet )