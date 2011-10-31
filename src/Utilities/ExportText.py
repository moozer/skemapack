'''
Created on Sep 13, 2011

@author: morten
'''

import sys, datetime
from Datatypes.EventFunctions import ReadEvent, MakeEventText
from Configuration.CommandLineOptions import ReadOptions
from string import Template

# TODO: move me.
#def ReadEvent(str, config):
#    EventDict = {}
#    for pair in str.split('; '):
#        if pair[-1] == '\n':
#            continue
#        (key, value) = pair.split(': ', 1)
#        EventDict[key.strip()] = value.strip()
#
#    Event = { 
#             'Date': datetime.datetime.strptime(EventDict['Date'], config['Dateformat']),
#             'Hours': (datetime.datetime.strptime(EventDict['StartTime'], config['Dateformat']+" %H:%M:%S"), 
#                       datetime.datetime.strptime(EventDict['EndTime'], config['Dateformat']+" %H:%M:%S")),
#             'Location': EventDict['Location'],
#             'Class': EventDict['Class'],
#             'Subject': EventDict['Subject']
#             }
#    return Event

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
#          'TeacherId': 5421,
#          'FirstWeek': 33,
#          'LastWeek': 52,
#          'Year': 2011,
#          'Dateformat': u"%Y-%m-%d",
#          'OutputDateformat': u"%Y-%m-%d",
#          'Subject': u'System Design',
#          'Class': u'11OIT3bH2'
#          }
#    return config
    
def ExportText( config, ConfigSet = "ExportText" ):
    EventCount = 0
    print "## Formatted output of event: %s"%(config.get(ConfigSet, 'Template'))
    
    OutTemplate = Template( config.get(ConfigSet, 'Template') )
    
    PrevEvent = None
    Multiple = 1
    
    for line in sys.stdin.readlines():
        Event = ReadEvent(line, config, ConfigSet)
            
        if PrevEvent is None:
            PrevEvent = Event
            continue

        EventCount += 1
        
        # current event date
        datestr = Event['Hours'][0].strftime(config.get( ConfigSet, 'OutputDateformat'))
        
        if datestr == PrevEvent['Hours'][0].strftime(config.get( ConfigSet, 'OutputDateformat')):
            Multiple += 1
        else:
            ET = MakeEventText( PrevEvent, config.get( ConfigSet, 'OutputDateformat') )
            ET['EventCount'] = EventCount-1
            ET['Multiplicity'] = Multiple
            print OutTemplate.substitute(ET)
#            print "%d-%d\t%s\t%s (%d)"%(EventCount-Multiple,EventCount-1,
#                                 PrevEvent['Class'], 
#                                 PrevEvent['Hours'][0].strftime(config['OutputDateformat']),
#                                 Multiple)
            Multiple = 1
            
        PrevEvent = Event
    
    if PrevEvent is not None:
        ET = MakeEventText( PrevEvent, config.get( ConfigSet, 'OutputDateformat') )
        ET['EventCount'] = EventCount
        ET['Multiplicity'] = Multiple
        print OutTemplate.substitute(ET)
#        print "%d-%d\t%s\t%s (%d)"%(EventCount-Multiple+1,EventCount,
#                         PrevEvent['Class'], 
#                         PrevEvent['Hours'][0].strftime(config['OutputDateformat']),
#                         Multiple)
        
if __name__ == '__main__':
    # TODO: implement an argument switch to handle changing stdin to read from file
    sys.stdin = file('../testpackage/Utilities/testdata/FilteredEventData.txt')
    
    # 1) read config/parameter
    # none yet

    # 2) receive config
    config = ReadOptions()

    # 3) print config
    # PrintConfig( config )
        
    # 4) receive events and output them
    ExportText( config )
    
