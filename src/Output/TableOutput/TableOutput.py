'''
Created on Nov 7, 2010

@author: morten
'''
import textile

class TableOutput(object):
    '''
    Using an iterable object returning a proper dictionary, it builds a textile  table 
    '''
    # TODO: TableOutput should be converted to a function.

    def __init__(self, ItObject, IncludeHeader=True, IncludeColumnSums = False ):
        '''
        Constructor
        '''
        self._ItObject = ItObject
        self._HeaderElements = ['Class','Teacher', 'Course']
        self._WeeklistKey = 'Lessons by week'
        self._TextileTable = ""
        self._IncludeHeader = IncludeHeader
        self._IncludeColumnSums = IncludeColumnSums
    
    def GetTextileTable(self, StartWeek=38, EndWeek=52 ):
        ''' Loops through the data and builds a textile table '''
        TTable = ""
        FirstEntry = True
        Sums = {}
        WeekNo = range(StartWeek, EndWeek)
        for entry in self._ItObject:
            if self._IncludeHeader:
                # first entry to be used for header titles (course, teacher etc) 
                if FirstEntry:
                    for e in self._HeaderElements:
                        if e in entry:
                            TTable += "|. " + e
                    if self._WeeklistKey in entry:
                        TTable += ''.join( [ '|'+str(Week) for Week in WeekNo] )
                    TTable += "|\n"
                    FirstEntry = False

            # column sum
            for e in self._HeaderElements:
                if e in entry:
                    TTable += "|. " + entry[e]
            if self._WeeklistKey in entry:
                for Week in WeekNo:
                    TTable += "|"
                    if Week in entry[self._WeeklistKey].keys(): 
                        TTable += str(entry[self._WeeklistKey][Week])
                        if str(Week) in Sums:
                            Sums[str(Week)] = entry[self._WeeklistKey][Week] + Sums[str(Week)]
                        else:
                            Sums[str(Week)] = entry[self._WeeklistKey][Week]
            
            TTable += "|\n"
        
        # append column sums.
        if self._IncludeColumnSums:
            for e in self._HeaderElements:
                TTable += "|"
            for Week in WeekNo:
                TTable += "|"
                if str(Week) in Sums:
                    TTable += str( Sums[str(Week)])
            TTable += "|\n"            
            
        self._TextileTable = TTable
        return TTable

    def GetHtmlTable(self, StartWeek=38, EndWeek=52):
        ''' Converts the textile to html '''
        self.GetTextileTable( StartWeek, EndWeek)
        result = textile.textile( self._TextileTable)
        return result
    