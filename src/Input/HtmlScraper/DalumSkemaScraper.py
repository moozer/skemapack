'''
Created on Nov 14, 2010

@author: morten
'''

import BeautifulSoup, datetime
from TableIterator import TableIterator

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
        self._WeekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self._Dates = {}
        self._DateFormat = "%d-%m-%y"
        
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
        ''' @return The data in the HTML buffer '''
        return self._HtmlData
    
    def GetDates(self):
        ''' @return The dates extracted from html '''
        return self._Dates
    
    def GetAppointments(self):
        ''' @return the extracted appointments '''
        return self._Appointments
    
    def ExtractAppointments(self):
        ''' Starts the parsing
        @return The number of appointments extracted '''
        ti = TableIterator( self._HtmlData )

        self._Lessons = []
        IsFirstRow = True
        for row in TableIterator( self._HtmlData ):
            if IsFirstRow:
                self._ProcessFirstRow( row )
                IsFirstRow = False
                continue
            try:
                self._Lessons.append( self._ProcessLessons( row ) )
            except ValueError:
                continue
        
        self._ConvertToApp()
        return len( self._Appointments )
    
    def _ProcessFirstRow(self, Row):
        ''' First row is special. It contains the dates. '''
        
        for i in range(1,6):
            self._Dates[self._WeekDays[i-1]] = datetime.datetime.strptime( Row[i].split(" ")[1], self._DateFormat )

    def _ProcessLessons(self, Row):
        ''' Lessons are retrieved horizontally '''
        Result = {}

        # lessons start and end times
        Time = Row[0].split('-')
        if len(Time) != 2:
            raise ValueError("Failed to convert time. End-of-list?")
        Result['LessonStart'] = Time[0].split(":")
        Result['LessonEnd'] = Time[1].split(":")
        
        for i in range(0,5):
            Result[self._WeekDays[i]] = (Row[3*i+1], Row[3*i+2], Row[3*i+3])
        
        return Result

    def _ConvertToApp(self):
        ''' converts self._Dates and _Lessons to appointments '''
        self._Appointments = []
        SkipList = [u' .']
        for WeekDay in self._WeekDays:
            for Lesson in self._Lessons:
                if Lesson[WeekDay][0] not in SkipList:
                    LessonStart = self._Dates[WeekDay] \
                        + datetime.timedelta( hours=int(Lesson['LessonStart'][0]), minutes=int(Lesson['LessonStart'][1]))
                    LessonEnd = self._Dates[WeekDay] \
                        + datetime.timedelta( hours=int(Lesson['LessonEnd'][0]), minutes=int(Lesson['LessonEnd'][1]))
                    self._Appointments.append( {    
                                "Date": self._Dates[WeekDay],
                                "Hours": [LessonStart, LessonEnd], 
                                "Subject": Lesson[WeekDay][0],
                                "Class": Lesson[WeekDay][1],
                                "Location": Lesson[WeekDay][2]
                            } )

    