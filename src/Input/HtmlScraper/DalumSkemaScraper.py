'''
Created on Nov 14, 2010

@author: morten
'''

class DalumSkemaScraper():
    '''
    Get the schedule information from the dalum homepage system.
    e.g from http://80.208.123.243/uge%2035/3_1427.htm
    '''


    def __init__(self, Id ):
        '''
        Constructor
        '''
        self._Id = Id
        self._Source = "Web"
        self._HtmlData = ""
        self._Appointments = []
        
    def GetId(self):
        ''' @return The internal Id used '''
        return self._Id
        
    def IsSourceWeb(self):
        ''' If true, data is fetched from the web, 
        otherwise from data specified by SetHtml
        '''
        return (self._Source == "Web")

    def SetHtml(self, HtmlData ):
        ''' Sets the html data to be used for extracting appointments
        @param HtmlData: The data to parse
        '''
        self._HtmlData = HtmlData
        self._Source = "HTML"
        
    def GetHtml(self):
        ''' @return The data in the html buffer '''
        return self._HtmlData
    
    def ExtractAppointments(self):
        ''' Starts the parsing
        @return The number of appointments extracted '''
        return len( self._Appointments )
    
    
    