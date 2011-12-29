'''
Created on Dec 29, 2011

@author: morten
'''

from Configuration.CommandLineOptions import ReadOptions
import sys
from Output.IcsOutput.IcsOutput import IcsOutput
from Datatypes.EventFunctions import ReadEvent

def ExportIcs( config, ConfigSet = "ExportIcs" ):
    ''' Configuration items needed are the same as for ReadEvent() 
        and 'OutputFile', 'InputFile'
    @param Config: the configuration object to use
    @param ConfigSet: The sub set of the configuration object.
    '''
    Events = []
    
    infile = config.get( ConfigSet, 'InputFile' )
    sys.stderr.write( "ExportIcs imput from file: %s" % ( infile ,) )
    fin = open( infile, "r")
        
    for line in fin.readlines():
        Event = ReadEvent(line, config, ConfigSet)
        if Event is not None:
            Events.append( Event )
        
    io = IcsOutput( Events )

    # save to file or stdout as specified in the config.
    outfile = config.get( ConfigSet, 'OutputFile' )
    sys.stderr.write( "ExportIcs output to file: %s" % ( outfile ,) )
    f = open( outfile, "wb" )
    f.write( io.GetIcsString() )
    f.close()
    
if __name__ == '__main__':
    # TODO: implement an argument switch to handle changing stdin to read from file
    sys.stdin = file('../testpackage/Utilities/testdata/SdeSkemaEventData.txt')
    
    # 1) read config/parameter
    # none yet

    # 2) receive config
    config = ReadOptions( Silent = True)

    # 3) print config
    # PrintConfig( config )
        
    # 4) receive events and output them
    ExportIcs( config )
    