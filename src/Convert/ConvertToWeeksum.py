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

    # loop over all events and do the sum.    
    for event in events:
        Year, Week, Weekday = event['Date'].isocalendar()
        
        if not Year in Weeksum.keys():
            Weeksum[Year] = {}
            
        if not Week in Weeksum[Year].keys():
            Weeksum[Year][Week] = {}
            
        if not event['Subject'] in Weeksum[Year][Week].keys():
            Weeksum[Year][Week][event['Subject']] = {}

        if not event['Class'] in Weeksum[Year][Week][event['Subject']].keys():
            Weeksum[Year][Week][event['Subject']][event['Class']] = 0

        Weeksum[Year][Week][event['Subject']][event['Class']] += 1

    # and convert to nice iterable list
    Result = []
    for Year in Weeksum.keys():
        for Week in Weeksum[Year].keys():
            for Subject in Weeksum[Year][Week].keys():
                for Class in Weeksum[Year][Week][Subject].keys():
                    entry = { 'Year': Year, 'Week': Week, 
                              'Subject': Subject, 'Class': Class,
                              'LessonCount': Weeksum[Year][Week][Subject][Class]}
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
    
    # output to file
    ExportFile( Events, config, ConfigSet )