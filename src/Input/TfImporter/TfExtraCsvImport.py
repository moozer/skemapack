'''
Created on Mar 3, 2011

@author: morten
'''

import os, csv

class TfExtraCsvImport:
    '''
    classdocs
    '''


    def __init__(self, Filename):
        '''
        Constructor
        '''
        if not Filename or not os.path.exists(Filename):
            raise ValueError( "CSV file not found: %s"%Filename)
        
        self._InputFile = Filename
        
        self._CsvDelimiter = '\t'
        self._InitSearchParams()
        
    def __iter__(self):
        ''' system stuff for iterators '''
        return self

    def _InitSearchParams(self):
        ''' inits the variables needed in the search '''
        self._WeekNoByColumn = {}
        self._TfReader = {}
        
    def _RetrieveLessonsByWeek(self, row):
        ''' returns the lessons by week for the current course '''
        Lessons = {}
        for Week in self._WeekNoByColumn.keys():
            Column = self._WeekNoByColumn[Week]
            try:
                if int( row[Column] ) > 0:
                    Lessons[Week] = int( row[Column] )       
            except:
                pass
            # else we don't include it
        
        if len( Lessons.keys() ) > 0:
            return Lessons
 
        return {}
    
    def _RetrieveWeekNumbers(self, row ):
        ''' based on the row, a new WeekNoByColumn is generated '''
        ColumnCount = 0
        WeekColumns = {}
        for entry in row: #@UnusedVariable
            ColumnCount += 1
 
            try:           
                WeekColumns[int( entry ) ] = ColumnCount
            except: 
                pass
            
        if len( WeekColumns ) > 0:
            self._WeekNoByColumn = WeekColumns
        # else keep the current values
        
    def GetCsvFilename(self):
        ''' Returns the name of the file being read '''
        return self._InputFile
    
    def IsSearchEnabled(self):
        ''' if true, system is ready to return entries '''
        return self._IsSearchEnabled;
       
    def EnableImportByTeacher( self, TeacherInitials ):
        '''
        Reset the search for lecture based on a specific teacher
        '''
        self._InitSearchParams()
        self._TeacherToSearchFor = TeacherInitials
        self._ClassToSearchFor = None
        self._TfReader = csv.reader(open(self._InputFile, "r"), delimiter=self._CsvDelimiter, quotechar='\"')
        self._IsSearchEnabled = True
   
    def EnableImportByClass( self, ClassName ):
        '''
        Reset the search for lecture based on a specific class
        '''
        self._InitSearchParams()
        self._ClassToSearchFor = ClassName
        self._TeacherToSearchFor = None
        self._TfReader = csv.reader(open(self._InputFile, "r"), delimiter=self._CsvDelimiter, quotechar='\"')
        self._IsSearchEnabled = True
        
    def next( self ):
        ''' 
        based on the current search method, the next entry found is returned
        returns empty list on eof
        '''
        
        # TODO: needs error handling
        for row in self._TfReader:
            if row[0] == "":
                self._RetrieveWeekNumbers(row)
                continue
            
            Teacher = row[0]
            Class = row[0]
            Project = row[1]
            LessonsByWeek = self._RetrieveLessonsByWeek(row)
            
            if (Teacher == self._TeacherToSearchFor or Class == self._ClassToSearchFor):
                return {'Teacher':  Teacher, 
                        'Class':    Class,
                        'Course':   Project,
                        'Lessons by week':   LessonsByWeek}

        # end iteration on file end.
        raise StopIteration
    