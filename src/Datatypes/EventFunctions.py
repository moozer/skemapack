'''
Created on Oct 29, 2011

@author: morten
'''

import datetime
import sys


def ReadEvent(InputText, DateFormat = "%Y-%m-%d"):
    ''' extracts event information from InputText
    Config needed is 'InputDateformat'
    @param InputText: text containing the event information
    @param config: configuration object to use.
    @param ConfigSet: The sub configuration to use
    @return: an Event dictionary with 'Date', 'Hours'[2], 'Location', 'Class' and 'Subject'
    '''
    NoEntriesInEvent = 6 # to avoid magic values
    
    if InputText[0] in ['#', '\n']:
        return None

    EventDict = {}
    for pair in InputText.split('; '):
        if pair[-1] == '\n':
            continue
        (key, value) = pair.split(': ', 1)
        EventDict[key.strip()] = value.strip()
        
    if len( EventDict) != NoEntriesInEvent:
        sys.stderr.write( "Bad line in input: '%s'\n"%(InputText) )
        return None
    
    Event = { 
             'Date': datetime.datetime.strptime(EventDict['Date'], DateFormat ),
             'Hours': [datetime.datetime.strptime(EventDict['StartTime'], DateFormat+" %H:%M:%S"), 
                       datetime.datetime.strptime(EventDict['EndTime'], DateFormat+" %H:%M:%S")],
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
    
def MakeEventString( event, DateFormat  ):
    EvStr = ""
    EventT = MakeEventText(event, DateFormat )
    for key in ['Date', 'StartTime', 'EndTime', 'Location', 'Class', 'Subject']:
        EvStr += "%s: %s; "%(key, EventT[key])
    EvStr += "\n" # adding final newline
    return EvStr
    
# TODO: Events should be a data type with event.__str__()
# TODO: implement output to file based on config
def WriteEvents( events, config, ConfigSet  ):
    
    for event in events:
        EventT = MakeEventText(event, config.get( ConfigSet, 'OutputDateformat') )
        for key in ['Date', 'StartTime', 'EndTime', 'Location', 'Class', 'Subject']:
            print "%s: %s;"%(key, EventT[key]),
        print "" # adding final newline
        