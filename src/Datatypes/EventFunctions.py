'''
Created on Oct 29, 2011

@author: morten
'''

import datetime


def ReadEvent(InputText, config):
    EventDict = {}
    for pair in InputText.split('; '):
        if pair[-1] == '\n':
            continue
        (key, value) = pair.split(': ', 1)
        EventDict[key.strip()] = value.strip()
        
    if len( EventDict) != 6:
        print "Bad line in input: '%s'"%(InputText)
        print EventDict
        return {}
    
    Event = { 
             'Date': datetime.datetime.strptime(EventDict['Date'], config['Dateformat']),
             'Hours': (datetime.datetime.strptime(EventDict['StartTime'], config['Dateformat']+" %H:%M:%S"), 
                       datetime.datetime.strptime(EventDict['EndTime'], config['Dateformat']+" %H:%M:%S")),
             'Location': EventDict['Location'],
             'Class': EventDict['Class'],
             'Subject': EventDict['Subject']
             }
    return Event

# TODO: Events should be a data type with event.__str__()
# TODO: implement output to file based on config
def WriteEvents( events, config, ConfigSet  ):
        
    for event in events:
        print "Date: %s;"%(event['Date'].strftime( config.get( ConfigSet, 'OutputDateformat'))),
        print "StartTime: %s;"%(event['Hours'][0].strftime( config.get( ConfigSet, 'OutputDateformat') +" %H:%M:%S")),
        print "EndTime: %s;"  %(event['Hours'][1].strftime( config.get( ConfigSet, 'OutputDateformat') +" %H:%M:%S")),
        print "Location: %s;"%(event['Location']),
        print "Class: %s;"%(event['Class']),
        print "Subject: %s;"%(event['Subject']),
        print "" # adding final newline