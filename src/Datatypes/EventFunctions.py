'''
Created on Oct 29, 2011

@author: morten
'''

import datetime
import sys

def LineParse( InputText ):
    ''' basic cehck and split of line into elements '''
    if InputText[0] in ['#', '\n']:
        return None

    EventDict = {}
    for pair in InputText.split('; '):
        if pair[-1] == '\n':
            continue
        (key, value) = pair.split(': ', 1)
        EventDict[key.strip()] = value.strip()
    
    return EventDict

def ReadString(InputText, DateFormat = "%Y-%m-%d"):
    ''' extracts event information from InputText
    Config needed is 'InputDateformat'
    @param InputText: text containing the event information
    @param config: configuration object to use.
    @param ConfigSet: The sub configuration to use
    @return: a Weeksum dictionary 
            or an Event dictionary with 'Date', 'Hours'[2], 'Location', 'Class', 'Subject', 'Teacher'
    '''
    NumEntriesInEvent = 7 # to avoid magic values
    NumEntriesInWeeksum = 6 # to avoid magic values
    
    EventDict = LineParse( InputText )
        
    if not EventDict:
        return None
    
    if len( EventDict) == NumEntriesInEvent:
        Event = { 
             'Date': datetime.datetime.strptime(EventDict['Date'], DateFormat ).date(),
             'Hours': [datetime.datetime.strptime(EventDict['StartTime'], DateFormat+" %H:%M:%S"), 
                       datetime.datetime.strptime(EventDict['EndTime'], DateFormat+" %H:%M:%S")],
             'Location': EventDict['Location'],
             'Class': EventDict['Class'],
             'Subject': EventDict['Subject'],
             'Teacher': EventDict['Teacher']
             }
        return Event
    elif len( EventDict) == NumEntriesInWeeksum:
        Ws = { 
             'Year':        int(EventDict['Year']),
             'Week':        int(EventDict['Week']),
             'LessonCount': int(EventDict['LessonCount']),
             'Class':       EventDict['Class'],
             'Subject':     EventDict['Subject'],
             'Teacher':     EventDict['Teacher']
             }
        return Ws
    
    sys.stderr.write( "failed to interpret line: %s"%InputText)


def MakeEventText(  event, DateFormat ):
    EventText = {   'Date':       event['Date'].strftime( DateFormat ),
                    'StartTime':  event['Hours'][0].strftime( DateFormat +" %H:%M:%S"),
                    'EndTime':    event['Hours'][1].strftime( DateFormat +" %H:%M:%S"),
                    'Location':   event['Location'],
                    'Class':      event['Class'],
                    'Subject':    event['Subject'],
                    'Teacher':    event['Teacher']                             
                 }
    return EventText
    
def MakeEventString( event, DateFormat  ):
    EvStr = ""
    EventT = MakeEventText(event, DateFormat )
    for key in ['Date', 'StartTime', 'EndTime', 'Location', 'Class', 'Subject', 'Teacher']:
        EvStr += "%s: %s; "%(key, EventT[key])
    EvStr += "\n" # adding final newline
    return EvStr
    
# TODO: Events should be a data type with event.__str__()
# TODO: implement output to file based on config
def WriteEvents( events, config, ConfigSet  ):
    
    for event in events:
        EventT = MakeEventText(event, config.get( ConfigSet, 'OutputDateformat') )
        for key in ['Date', 'StartTime', 'EndTime', 'Location', 'Class', 'Subject', 'Teacher']:
            print "%s: %s;"%(key, EventT[key]),
        print "" # adding final newline
        
## ------ weeksum stuff below
def MakeWeeksumText( Weeksum, DateFormat ):
    EventText = {   'Year':         int(Weeksum['Year']),
                    'Week':         Weeksum['Week'],
                    'LessonCount':  int(Weeksum['LessonCount']),
                    'Class':        Weeksum['Class'],
                    'Subject':      Weeksum['Subject'],
                    'Teacher':      Weeksum['Teacher']                             
                 }
    return EventText

def MakeWeeksumString( Weeksum, DateFormat  ):
    WsStr = ""
    EventT = MakeWeeksumText(Weeksum, DateFormat )
    for key in ['Year', 'Week', 'LessonCount', 'Class', 'Subject', 'Teacher']:
        WsStr += "%s: %s; "%(key, EventT[key])
    WsStr += "\n" # adding final newline
    return WsStr
    
# activity data conversion
def AdToWeeksum( Ad ):
    WsBase = { 
             'Year':        0,
             'Week':        0,
             'LessonCount': 0,
             'Class':       Ad.getClass(),
             'Subject':     Ad.getCourse(),
             'Teacher':     Ad.getTeacher()
             }
    WsList = []
    
    for WeekNo in Ad.getListOfWeeks():
        # sys.stderr.write( "Year is hardcoded to 2012\n" )
        # todo: Year could be removed, but it might break stuff elsewhere...
        WsBase['Year'] = int(WeekNo.split('-')[0])
        WsBase['Week'] = WeekNo
        WsBase['LessonCount'] = Ad.getLessons(WeekNo)
        WsList.append( WsBase.copy() )
    return WsList
    