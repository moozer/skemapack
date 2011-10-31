'''
Created on Oct 30, 2011

@author: morten
'''

from Datatypes.EventFunctions import ReadEvent
from Datatypes.EventFunctions import WriteEvents
import sys
from Configuration.CommandLineOptions import ReadOptions
from ConfigParser import NoSectionError

#def ReceiveConfig():
#    config = {}
#
#    while( True ):
#        line = sys.stdin.readline();
#        if not line.startswith('#'):
#            break
#        
##        if line == '\n':
##            break
#        
#        # and do some parsing...
#        #        
#        #        line = line.lstrip('#')
#        #        pair = line.split( "=", 1)
#        #     config[pair[0]] = pair[1]
#        ''
#    config = { 
#          'Dateformat': u"%Y-%m-%d",
#          'OutputDateformat': u"%Y-%m-%d",
#          'Subject': u'System Design',
#          'Class': u'11OIT3bH2'
#          }
#    return config

def FilterOnKey( Event, Key, config, ConfigSet  ):
    if Event is None:
        return Event
    
    try:
        val = config.get( ConfigSet, Key )
        if Event[Key] == val:
            return Event
        else:
            return None
    except NoSectionError:
        # no config for this key, so just accept the event
        return Event
    

def EventFilter( config, ConfigSet = "Filter" ):
    Events = []
    
    for key in ['Subject', 'Class']:
        try:
            val = config.get( ConfigSet, key )
            print "## Listing all events with '%s' being '%s'"%(key, val)
        except NoSectionError:
            print "## not filtering on %s"%key


    for line in sys.stdin.readlines():
        Event = ReadEvent(line, config, ConfigSet )
        for key in ['Subject', 'Class']:
            Event = FilterOnKey( Event, key, config, ConfigSet )
        
        if Event is not None:
            Events.append(Event)
    
    return Events

if __name__ == '__main__':
    # TODO: implement an argument switch to handle changing stdin to read from file
    sys.stdin = file('../testpackage/Utilities/testdata/SdeSkemaEventData.txt')
    
    # 1) read config/parameter
    # none yet

    # 2) receive config
    config = ReadOptions()

    # 3) print config
    # PrintConfig( config )
        
    # 4) receive events and output them
    Events = EventFilter( config )
    WriteEvents( Events, config, "Filter" )

