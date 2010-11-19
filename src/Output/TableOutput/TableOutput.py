'''
Created on Nov 7, 2010

@author: morten
'''
import textile

class TableOutput(object):
    '''
    Using an iterable object returning a proper dictionary, it builds a textile  table 
    '''
    # TODO: TableOutput should be converted to a function
    # TODO: Tableoutput should not use textile, maybe... TBD

    def __init__(self, ItObject, IncludeHeader=True, IncludeColumnSums = False, IncludeRowSums = False ):
        '''
        Constructor
        '''
        self._ItObject = ItObject
        self._HeaderElements = ['Class','Teacher', 'Course']
        self._WeeklistKey = 'Lessons by week'
        self._TextileTable = ""
        self._IncludeHeader = IncludeHeader
        self._IncludeColumnSums = IncludeColumnSums
        self._IncludeRowSums = IncludeRowSums
    

    def _GenerateHeader(self, WeekNo, entry, IncludeRowSums):
        ''' Generates the header line
        @param WeekNo: The list of weeks to include 
        @param entry: An entry. Used for non-week columns.
        @return: the table text for the header part.
        ''' 
        TTable = ""
        for e in self._HeaderElements:
            if e in entry:
                TTable += "|. " + e
        
        if self._WeeklistKey in entry:
            TTable += ''.join(['|' + str(Week) for Week in WeekNo])

        if IncludeRowSums:
            TTable += "|. " + "Sum"
        
        TTable += "|\n"
        return TTable


    def _GenerateColumnSumsLine(self, ColumnSums, WeekNo ):
        ''' Generates the bottom line with the sums
        @param WeekNo: The list of weeks to include 
        @param ColumnSums: The dictionary which holds the sums.
        @return: the table text for the header part.
        ''' 
        TTable = ""
        if self._IncludeColumnSums:
            for e in self._HeaderElements: #@UnusedVariable
                TTable += "|"
            
            for Week in WeekNo:
                TTable += "|"
                if str(Week) in ColumnSums:
                    TTable += str(ColumnSums[str(Week)])
            
            TTable += "|\n"
        return TTable


    def _GenerateTableEntries(self, ColumnSums, WeekNo, entry, IncludeRowSums):
        ''' Generates the lines with the course info
        @param WeekNo: The list of weeks to include 
        @param ColumnSums: The dictionary which holds the sums (to be updated)
        @param entry: the course entry
        @return: the table text for the header part.
        ''' 
        TTable = ""
        RowSum = 0
        
        # Course name, teacher name, etc.
        for e in self._HeaderElements:
            if e in entry:
                TTable += "|. " + entry[e]

        # check if the entry holds actual course data.
        if not self._WeeklistKey in entry:
            raise ValueError("yes, this is a bit extreme, but it works.")

        # the weeks
        for Week in WeekNo:
            TTable += "|"
            if Week in entry[self._WeeklistKey].keys():
                TTable += str(entry[self._WeeklistKey][Week])
                RowSum += entry[self._WeeklistKey][Week]
                if str(Week) in ColumnSums:
                    ColumnSums[str(Week)] += entry[self._WeeklistKey][Week]
                else:
                    ColumnSums[str(Week)] = entry[self._WeeklistKey][Week]
        
        # add the sum cell if applicable
        if IncludeRowSums:
            TTable += "|" + str(RowSum)
        
        TTable += "|\n"
        return TTable

    def GetTextileTable(self, StartWeek=38, EndWeek=52 ):
        ''' Loops through the data and builds a textile table '''
        TTable = ""
        FirstEntry = True
        ColumnSums = {}
        WeekNo = range(StartWeek, EndWeek)
        for entry in self._ItObject:
            # first entry to be used for header titles (course, teacher etc)
            if self._IncludeHeader and FirstEntry:
                TTable += self._GenerateHeader(WeekNo, entry, self._IncludeRowSums)
                FirstEntry = False
            # other entries
            TTable += self._GenerateTableEntries(ColumnSums, WeekNo, entry, self._IncludeRowSums)
        
        # append column sums.
        if self._IncludeColumnSums:
            TTable += self._GenerateColumnSumsLine(ColumnSums, WeekNo)            
            
        self._TextileTable = TTable
        return TTable

    def GetHtmlTable(self, StartWeek=38, EndWeek=52):
        ''' Converts the textile to html '''
        self.GetTextileTable( StartWeek, EndWeek)
        result = textile.textile( self._TextileTable)
        return result
    