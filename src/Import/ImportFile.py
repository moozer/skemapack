'''
Created on 28 Jan 2012

@author: moz
'''
from Datatypes.EventFunctions import WriteEvents, ReadEvent
from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin
import sys


def ImportFile( config, ConfigSet = "ImportFile" ):
    # read data from file or net
    fp = open(config.get(ConfigSet, "Infile"))

    Events = []
    for EventText in fp:
        event = ReadEvent(EventText, config, ConfigSet)
        if not event:
            continue
        
        Events.append( event )

    return  Events 


if __name__ == '__main__':

    if len(sys.argv) > 2:
        cfgfile = sys.argv[1]
    else:
        cfgfile = SkemaPackConfig_stdin()

#    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "SkemaScraper"

    # 3) import from skema
    Events = ImportFile( config, ConfigSet )
    
    # 4) output all events to stdout
    print config # placed here to allow config to be changed...
    WriteEvents( Events, config, ConfigSet )