'''
Created on Nov 7, 2010

@author: morten
'''
import textile

class TableOutput(object):
    '''
    Using an iterable object returning a proper dictionary, it builds a textile  table 
    '''

    def __init__(self, ItObject ):
        '''
        Constructor
        '''
        self._ItObject = ItObject
        self._HeaderElements = ['Class','Teacher', 'Course']
        self._HeaderWeeks = 'Lessons by week'
        self._TextileTable = ""
    
    def GetTextileTable(self, StartWeek=38, EndWeek=52):
        ''' Loops through the data and builds a textile table '''
        TTable = ""
        FirstEntry = True
        Sums = {}
        for entry in self._ItObject:
            # first entry to be used for headers 
            if FirstEntry:
                for e in self._HeaderElements:
                    if e in entry:
                        TTable += "|. " + e
                if self._HeaderWeeks in entry:
                    WeekNo = range(StartWeek, EndWeek)
                    TTable += ''.join( [ '|'+str(Week) for Week in WeekNo] )
                TTable += "|\n"
                FirstEntry = False
            
            for e in self._HeaderElements:
                if e in entry:
                    TTable += "|. " + entry[e]
            if self._HeaderWeeks in entry:
                for Week in WeekNo:
                    TTable += "|"
                    if Week in entry[self._HeaderWeeks].keys(): 
                        TTable += str(entry[self._HeaderWeeks][Week])
                        if str(Week) in Sums:
                            Sums[str(Week)] = entry[self._HeaderWeeks][Week] + Sums[str(Week)]
                        else:
                            Sums[str(Week)] = entry[self._HeaderWeeks][Week]
            
            TTable += "|\n"
        
        
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
    