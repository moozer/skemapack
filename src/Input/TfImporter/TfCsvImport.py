# -*- coding: UTF-8 -*-

'''
Created on Nov 6, 2010

@author: morten
'''
import csv, os
from Datatypes.ActivityData import ActivityData

class TfCsvImport():
    '''
    Import TF data from csv file 
    '''

    def __init__( self, CsvInputFilename, CsvDelimiter = "\t"):
        '''
        @param CsvInputFilename The file to retrieve data from.
        '''
        if not CsvInputFilename or not os.path.exists(CsvInputFilename):
            raise ValueError( "CSV file not found: %s"%CsvInputFilename)
            
        self._InputFile = CsvInputFilename
        self._IsSearchEnabled = False
 
        # needed for parsing 
        # constants
        self._NewClassKeywords = [u"ANTAL STUDERENDE:"]
        self._EndClassKeywords = [u"I ALT", u"I  ALT"]
        self._CsvDelimiter = CsvDelimiter
        self._LinenoWithWeekinfo = 2
        
        self._InitSearchParams()
 
    def __iter__(self):
        ''' system stuff for iterators '''
        return self
 
    def _InitSearchParams(self):
        ''' inits the variables needed in the search '''
        self._state = u'FILEHEADER'
        self._lineno = 0
        self._classStartLine = 0
        self._classEndLine = 0
        self._CurrentClass = ""
        self._CurrentTeacher = ""
        self._CurrentCourse = ""
        self._WeekNoByColumn = {}
        
# --- get/set functions --
    def GetCsvFilename( self ):
        ''' returns the csv file specified for input '''
        return self._InputFile
    
    def IsSearchEnabled(self):
        ''' if true, system is ready to return entries '''
        return self._IsSearchEnabled;
    
    def GetMetaData(self):
        ''' returns information about the search and the csv file '''
        return { 'Csv cell delimiter': self._CsvDelimiter, 'Weeknumbers by column': self._WeekNoByColumn }
        
# --- other methods ---
    def EnableImportByTeacher( self, TeacherInitials ):
        '''
        Reset the search for lecture based on a specific teacher
        '''
        self._InitSearchParams()
        self._TeacherToSearchFor = TeacherInitials
        self._ClassToSearchFor = None
        self._AcceptAllActivities = False
        self._TfReader = csv.reader(open(self._InputFile, "r"), delimiter=self._CsvDelimiter, quotechar='\"')
        self._IsSearchEnabled = True
   
    def EnableImportByClass( self, ClassName ):
        '''
        Reset the search for lecture based on a specific class
        '''
        self._InitSearchParams()
        self._ClassToSearchFor = ClassName
        self._TeacherToSearchFor = None
        self._AcceptAllActivities = False
        self._TfReader = csv.reader(open(self._InputFile, "r"), delimiter=self._CsvDelimiter, quotechar='\"')
        self._IsSearchEnabled = True
             
    def EnableImportAll( self ):
        '''
        Reset the search and accept all activities
        '''
        self._InitSearchParams()
        self._ClassToSearchFor = None
        self._TeacherToSearchFor = None
        self._AcceptAllActivities = True
        self._TfReader = csv.reader(open(self._InputFile, "r"), delimiter=self._CsvDelimiter, quotechar='\"')
        self._IsSearchEnabled = True

    def next( self ):
        ''' 
        based on the current search method, the next entry found is returned
        returns empty list on eof
        '''
        
        # TODO: needs error handling
        for row in self._TfReader:

            try:
                row = [unicode(col, 'utf-8') for col in row]
            except:
                raise ValueError( "Failed to convert csv data to unicode on line %d: %s" % (self._TfReader.line_num, str(row)) )
            
            self._lineno += 1
            if self._state in [u'FILEHEADER',  u'NEXTCLASS']:
                self._DoStateFileHeader( row )
            
            if self._state == u'CLASSHEADER':
                if self._lineno ==  self._classStartLine+1:
                    self._CurrentClass = row[0]
                if self._lineno - 2 > self._classStartLine :
                    self._state = u'INCLASS'
            
            if self._state == u'INCLASS':
                if row[0] in self._EndClassKeywords :
                    self._state = u'CLASSFOOTER'
                    self._classEndLine = self._lineno
                else: 
                    if len(row) > 5 :
                        self._CurrentTeacher = row[5]
                        self._CurrentCourse = row[0]
            
            if self._state == u'CLASSFOOTER':
                if  self._lineno  > self._classEndLine:
                    self._state = u'NEXTCLASS'

            # if we have a match, return the line        
            if self._state in [u'INCLASS']:
                if self._CurrentTeacher == '':
                    continue
                if self._CurrentClass == '':
                    continue
                
                if (    self._CurrentTeacher == self._TeacherToSearchFor 
                    or  self._CurrentClass == self._ClassToSearchFor
                    or  self._AcceptAllActivities):
                    return ActivityData(  Teacher =  self._CurrentTeacher, 
                                        Class =    self._CurrentClass,
                                        Course =   self._CurrentCourse,
                                        LessonsList = self._RetrieveLessonsByWeek(row) )

        # end iteration on file end.
        raise StopIteration
    
                    
    def GetNextEntryIterator( self ):
        ''' 
        based on the current search method, the next entry found is yielded
        raise StopIteration when done
        '''
        
        # TODO: needs error handling
        for row in self._TfReader:

            row = [unicode(col) for col in row]

            self._lineno += 1
            if self._state in [u'FILEHEADER',  u'NEXTCLASS']:
                self._DoStateFileHeader( row )
            
            if self._state == u'CLASSHEADER':
                if self._lineno ==  self._classStartLine+1:
                    self._CurrentClass = row[0]
                if self._lineno - 2 > self._classStartLine :
                    self._state = u'INCLASS'
            
            if self._state == u'INCLASS':
                if row[0] in self._EndClassKeywords :
                    self._state = u'CLASSFOOTER'
                    self._classEndLine = self._lineno
                else: 
                    if len(row) > 5 :
                        self._CurrentTeacher = row[5]
                        self._CurrentCourse = row[0]
            
            if self._state == u'CLASSFOOTER':
                if  self._lineno  > self._classEndLine:
                    self._state = u'NEXTCLASS'

            # if we have a match, return the line        
            if self._state in [u'INCLASS']:
                if self._CurrentTeacher == self._TeacherToSearchFor:
                    yield ActivityData( self._CurrentTeacher, self._CurrentClass,
                                        self._CurrentCourse, self._RetrieveLessonsByWeek(row) )
        raise StopIteration
    
    def _DoStateFileHeader(self, row ):
        ''' handles extracting info in state FILEHEADER and NEXTCLASS '''
        if len(row) > 5 :
            # extract week numbers by columns
            if self._lineno == self._LinenoWithWeekinfo:
                LastWeekNo = 0 # to check for increasing weeknumbers
                for ColumnNo in range(0, len(row) ):
                    cell = row[ColumnNo]
                    QuitOnNextError = False
                    try:
                        # enforce increasing week numbers
                        if not int(cell) > LastWeekNo:
                            return
                                                                                                
                        self._WeekNoByColumn[int(cell)] = ColumnNo
                        QuitOnNextError = True
                    except( ValueError ):
                        if QuitOnNextError:
                            return
                return
                
            if row[0] in self._NewClassKeywords :
                self._state = u'CLASSHEADER'
                self._classStartLine = self._lineno
            if  row[5] == u'LÆRER':
                self._state = u'CLASSHEADER'
                self._classStartLine = self._lineno - 1

    def _RetrieveLessonsByWeek(self, row):
        ''' returns the lessons by week for the current course '''
        Lessons = {}
        for Week in self._WeekNoByColumn.keys():
            Column = self._WeekNoByColumn[Week]
            try:
                if int( row[Column] ) > 0:
                    Lessons[Week] = int( row[Column] )       
            except( ValueError ):
                pass
            # else we don't include it
        
        if len( Lessons.keys() ) > 0:
            return Lessons
 
        return {}
        