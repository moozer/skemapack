'''
Created on Sep 7, 2011

@author: morten
'''
try:
    from icalendar import Event, Calendar
except:
    print "Icalendar import error"
    print "Get the module from http://codespeak.net/icalendar/"
    exit()

def IcsImport( IcsFileToUse ):
    '''
    @param IcsFileToUse: The file which contains the calendar entries
    '''
    f = open( IcsFileToUse, "r" )
    FileContent = f.read()
    
    cal = Calendar.from_string(FileContent)
    for event in cal.walk('vevent'):
        try:
            desc = event.decoded('description')
        except:
            desc = ""
        Entry = {'Description': desc,
                 'Summary': event.decoded('summary'),
                 'StartDate': event.decoded('dtstart'),
                 'EndDate': event.decoded('dtend')}
        yield Entry
    #raise StopIteration
