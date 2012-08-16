'''
Created on Aug 16, 2012

@author: moz
'''
from Import.ImportFile import ImportFile
from Configuration.SkemaPackConfig import SkemaPackConfig,\
    SkemaPackConfig_stdin_eal
import sys
from Output.CsvOutput import CsvOutput
import csv

def ExportCsv( Events, config, ConfigSet = "ExportCsv" ):
    ''' Configuration items needed are the same as for ReadEvent() 
        and 'OutputFile', 'InputFile'
    @param Events: the events to output 
    @param Config: the configuration object to use
    @param ConfigSet: The sub set of the configuration object.
    '''
        
    CsvList = CsvOutput( Events )

    # save to file or stdout as specified in the config.
    outfile = config.get( ConfigSet, 'OutFile' )
    d = config.get( ConfigSet, 'Delimiter' )

    f = open( outfile, "wb" )
    
    CsvWriter = csv.writer( f, delimiter = d)
    for row in CsvList:
        CsvWriter.writerow( row )
        
    f.close()
    
if __name__ == '__main__':
    # allow cfg file from cmd line
    if len(sys.argv) > 1:
        cfgfile = open( sys.argv[1] )
    else:
        cfgfile = SkemaPackConfig_stdin_eal()

    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "ExportCsv"

    # 3) import from file (which might be stdin
    Events = ImportFile( config, ConfigSet )
    
    # 4) output all events to ics
    ExportCsv( Events, config )
    
