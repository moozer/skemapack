'''
Created on Oct 29, 2011

@author: morten
'''

import datetime


def ReadEvent(InputText, config, ConfigSet):
    if InputText[0] in ['#', '\n']:
        return None
    
    EventDict = {}
    for pair in InputText.split('; '):
        if pair[-1] == '\n':
            continue
        (key, value) = pair.split(': ', 1)
        EventDict[key.strip()] = value.strip()
        
    if len( EventDict) != 6:
        print "Bad line in input: '%s'"%(InputText)
        print EventDict
        return None
    
    Event = { 
             'Date': datetime.datetime.strptime(EventDict['Date'], config.get( ConfigSet, 'InputDateformat' )),
             'Hours': (datetime.datetime.strptime(EventDict['StartTime'], config.get( ConfigSet, 'InputDateformat' )+" %H:%M:%S"), 
                       datetime.datetime.strptime(EventDict['EndTime'], config.get( ConfigSet, 'InputDateformat' )+" %H:%M:%S")),
             'Location': EventDict['Location'],
             'Class': EventDict['Class'],
             'Subject': EventDict['Subject']
             }
    return Event

def MakeEventText(  event, DateFormat ):
    EventText = {   'Date':       event['Date'].strftime( DateFormat ),
                    'StartTime':  event['Hours'][0].strftime( DateFormat +" %H:%M:%S"),
                    'EndTime':    event['Hours'][1].strftime( DateFormat +" %H:%M:%S"),
                    'Location':   event['Location'],
                    'Class':      event['Class'],
                    'Subject':    event['Subject']                              
                 }
    return EventText
    
    
# TODO: Events should be a data type with event.__str__()
# TODO: implement output to file based on config
def WriteEvents( events, config, ConfigSet  ):
        
    for event in events:
        EventT = MakeEventText(event, config.get( ConfigSet, 'OutputDateformat') )
        for key in ['Date', 'StartTime', 'EndTime', 'Location', 'Class', 'Subject']:
            print "%s: %s;"%(key, EventT[key]),
        print "" # adding final newline