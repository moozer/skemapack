'''
Created on Sep 13, 2011

@author: morten
'''

import sys, datetime

# TODO: move me.
def ReadEvent(str, config):
    EventDict = {}
    for pair in str.split('; '):
        if pair[-1] == '\n':
            continue
        (key, value) = pair.split(': ', 1)
        EventDict[key.strip()] = value.strip()

    Event = { 
             'Date': datetime.datetime.strptime(EventDict['Date'], config['Dateformat']),
             'Hours': (datetime.datetime.strptime(EventDict['StartTime'], config['Dateformat']+" %H:%M:%S"), 
                       datetime.datetime.strptime(EventDict['EndTime'], config['Dateformat']+" %H:%M:%S")),
             'Location': EventDict['Location'],
             'Class': EventDict['Class'],
             'Subject': EventDict['Subject']
             }
    return Event

def ReceiveConfig():
    config = {}

    while( True ):
        line = sys.stdin.readline();
        if not line.startswith('#'):
            break
        
#        if line == '\n':
#            break
        
        # and do some parsing...
        #        
        #        line = line.lstrip('#')
        #        pair = line.split( "=", 1)
        #     config[pair[0]] = pair[1]
        ''
    config = { 
          'TeacherId': 5421,
          'FirstWeek': 33,
          'LastWeek': 52,
          'Year': 2011,
          'Dateformat': u"%Y-%m-%d",
          'OutputDateformat': u"%Y-%m-%d",
          'Subject': u'Datacom.',
          'Class': u'11OIT3bH2'
          }
    return config
    
def ExportText( config ):
    EventCount = 0
    print "Listing all events with subject %s"%config['Subject']
    for line in sys.stdin.readlines():
        Event = ReadEvent(line, config)
        if Event['Subject'] == config['Subject']:
            EventCount += 1
            print "%d\t%s\t%s"%(EventCount,
                                Event['Hours'][0].strftime(config['OutputDateformat']),
                                Event['Class'])
        
if __name__ == '__main__':
    # TODO: implement an argument switch to handle changing stdin to read from file
    sys.stdin = file('../testpackage/Utilities/testdata/SdeSkemaEventData.txt')
    
    # 1) read config/parameter
    # none yet

    # 2) receive config
    config = ReceiveConfig()

    # 3) print config
    # PrintConfig( config )
        
    # 4) receive events and output them
    ExportText( config )
    
