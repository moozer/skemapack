'''
Created on Sep 13, 2011

@author: morten
'''

import sys

def ReadEvents(str):
    Event = {}
    for pair in str.split('; '):
        if pair[-1] == '\n':
            continue
        (key, value) = pair.split(': ', 1)
        Event[key.strip()] = value.strip()
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
          'Dateformat': u"%d-%m-%Y",
          'Subject': u'IT Security',
          'Class': u'11OIT3bH2'
          }
    return config
    
def ExportText( config ):
    EventCount = 0
    print "Listing all events with subject %s"%config['Subject']
    for line in sys.stdin.readlines():
        Event = ReadEvents(line)
        if Event['Subject'] == config['Subject']:
            EventCount += 1
            print "%d\t%s"%(EventCount,Event['Date'])
        
if __name__ == '__main__':
    sys.stdin = file('../testpackage/Utilities/testdata/SdeSkemaEventData.txt')
    
    # 1) read config/parameter
    # none yet

    # 2) receive config
    config = ReceiveConfig()

    # 3) print config
    # PrintConfig( config )
        
    # 4) receive events and output them
    ExportText( config )
    
