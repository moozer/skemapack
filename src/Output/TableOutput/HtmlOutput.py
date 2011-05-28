'''
Created on May 27, 2011

@author: morten
'''

class HtmlOutput():
    '''
    classdocs
    '''


    def __init__(self, ItObj, CmpObj = None ):
        '''
        Constructor
        '''
        self._ItObject = ItObj
        self._HeaderElements = ['Class','Teacher', 'Course']
        self._CmpObj = CmpObj
        self._CssClassEqual = "Equal"
        self._CssClassDiff = "NotEqual"
        
    def GetHtmlTable(self, StartWeek=1, EndWeek=52 ):
        ''' Loops through the data and builds the html table '''
        Html = "\t<table>\n"

        WeekNo = range(StartWeek, EndWeek+1)
        
        # primary iterator
        iterObj = iter( self._ItObject )
        entry = self._getNext(iterObj)
        
        # comparison iterator
        if self._CmpObj:
            iterCmpObj = iter(self._CmpObj)
            CmpEntry = self._getNext(iterCmpObj)
        else:
            CmpEntry = None
            iterCmpObj = None

        # first entry to be used for header titles (course, teacher etc)
        Html += self._GenerateHeader( WeekNo )                    
       
        # looping until both are None
        if self._CmpObj:
            while( CmpEntry or entry ):        
                EntryVal = entry.getCourse()
                CmpValue = CmpEntry.getCourse()
                
                if (not CmpEntry) or (EntryVal < CmpValue):
                    Html += self._GenerateTableEntries(WeekNo, entry, None )
                    entry = self._getNext(iterObj)
                elif (not entry) or (EntryVal > CmpValue):
                    Html += self._GenerateTableEntries(WeekNo, None, CmpEntry )
                    CmpEntry = self._getNext(iterCmpObj)                
                elif entry.getCourse() == CmpEntry.getCourse():
                    Html += self._GenerateTableEntries(WeekNo, entry, CmpEntry )
                    CmpEntry = self._getNext(iterCmpObj)
                    entry = self._getNext(iterObj)
                else:
                    raise ValueError("Should never get here!")
        else:
            while( entry ):        
                Html += self._GenerateTableEntries(WeekNo, entry, None )
                entry = self._getNext(iterObj)
                
        Html += "\t</table>\n"
        return Html
    
    def _getNext(self, iter ):
        # if iter is None, return None
        if not iter:
            return None
        
        try:
            NextEntry = iter.next()
        except StopIteration:
            NextEntry = None
        return NextEntry    

    def _GenerateTableEntries(self, WeekNo, entry, CmpEntry):
        ''' Generates the lines with the course info
        @param WeekNo: The list of weeks to include 
        @param entry: the course entry
        @return: the table text for the header part.
        ''' 
        TTable = "\t\t<tr>\n"
        
        # Course name, teacher name, etc.
        TTable += "\t\t\t<td>%s</td>\n" % entry.getClass()
        TTable += "\t\t\t<td>%s</td>\n" % entry.getTeacher()
        TTable += "\t\t\t<td>%s</td>\n" % entry.getCourse()

        # the weeks
        for Week in WeekNo:
            if Week in entry.getListOfWeeks():
                if not entry:
                    Content = self._CellContent( None, CmpEntry.getLessons(Week) ) 
                elif not CmpEntry:
                    Content = self._CellContent( entry.getLessons(Week), None ) 
                else:
                    Content = self._CellContent( entry.getLessons(Week), CmpEntry.getLessons(Week) ) 

                TTable += "\t\t\t<td>%s</td>\n" % Content
            else:
                TTable += "\t\t\t<td></td>\n"

        TTable += "\t\t</tr>\n"
        return TTable

    def _CellContent(self, EntryTxt, CmpEntryTxt ):
        if not self._CmpObj:
            return EntryTxt
        
        txt = "<table class=\"%s\">" % (self._CssClassEqual if EntryTxt == CmpEntryTxt else self.CssClassDiff )
        txt += "<tr><td>%s</td></tr><tr><td>%s</td></tr>" % (EntryTxt, CmpEntryTxt)
        txt += "</table>"
        return txt

    def _GenerateHeader(self, WeekNo ):
        ''' Generates the header line
        @param WeekNo: The list of weeks to include 
        @param entry: An entry. Used for non-week columns.
        @return: the table text for the header part.
        ''' 
        TTable = "\t\t<tr>\n"

        # Course name, teacher name, etc.
        for e in self._HeaderElements:
            TTable += "\t\t\t<td>%s</td>\n" % e
        
        # add all week columns
        TTable += ''.join(["\t\t\t<td>%s</td>\n" % str(Week) for Week in WeekNo])
        
        TTable += "\t\t</tr>\n"
        return TTable

