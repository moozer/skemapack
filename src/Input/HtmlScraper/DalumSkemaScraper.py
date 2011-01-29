'''
Created on Nov 14, 2010

@author: morten
'''

import datetime, urllib
from TableIterator import TableIterator

class DalumSkemaScraper():
    '''
    Get the schedule information from the dalum homepage system.
    e.g from http://80.208.123.243/uge%2035/3_1427.htm
    '''

    def __init__(self, Id, WeekNo = None ):
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
        self._WeekNo = WeekNo
        self._UrlToOpen = "(No URL)"
        
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
        ''' @return The dates from the latest week extracted from html '''
        return self._Dates
    
    def GetAppointments(self):
        ''' @return the extracted appointments '''
        return self._Appointments
    
    def ExtractAppointments(self, NonFatal = False):
        ''' Starts the parsing
        @param NonFatal: If false, then raise exception on bad first row, otherwise silently ignore entire week. Default false 
        @return The number of appointments extracted '''
        self._Appointments = []
        if self.IsSourceWeb():
            if not self._WeekNo:
                raise ValueError( "Week number must be supplied" )

            for WeekNo in self._WeekNo:
                self._RetrieveHtml( WeekNo )
                self._ProcessHtml( NonFatal )
        else:
            self._ProcessHtml( NonFatal )
        return len( self._Appointments )
    
    def _ProcessHtml(self, NonFatal):
        ''' Handles html parsing and convertions 
        @param NonFatal: If false, then raise exception on bad first row, otherwise silently ignore entire week. Default false 
        '''
        self._Lessons = []
        IsFirstRow = True
        for row in TableIterator( self._HtmlData ):
            if IsFirstRow:
                try:
                    self._ProcessFirstRow( row )
                except ValueError:
                    if NonFatal:
                        continue
                    raise
                IsFirstRow = False
                continue
            try:
                self._Lessons.append( self._ProcessLessons( row ) )
            except ValueError:
                continue
        
        self._ConvertToApp()
        
    
    def _ProcessFirstRow(self, Row):
        ''' First row is special. It contains the dates. '''
        try:
            for i in range(1,6):
                self._Dates[self._WeekDays[i-1]] = datetime.datetime.strptime( Row[i].split(" ")[1], self._DateFormat )
        except IndexError:
            raise ValueError( "Failed to extract dates from HTML. Check web page: %s"%self._UrlToOpen)

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
    
    def _RetrieveHtml( self, WeekNo ):
        ''' Retrieves the proper page based on week and Id '''
        if type( WeekNo ) != type( int(0) ):
            raise ValueError( "Bad Week number supplied" )
        
        self._UrlToOpen = "http://80.208.123.243/uge %i/3_%i.htm"%( WeekNo, self._Id )
        print "url: ", self._UrlToOpen
        usock = urllib.urlopen(self._UrlToOpen)
        self._HtmlData = usock.read()
        usock.close()
    