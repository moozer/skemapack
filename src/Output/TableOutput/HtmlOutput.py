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
                if not entry: # then CmpEntry is used.
                    Html += self._GenerateTableEntries(WeekNo, None, CmpEntry )
                    CmpEntry = self._getNext(iterCmpObj)
                    continue
                if not CmpEntry:
                    Html += self._GenerateTableEntries(WeekNo, entry, None )
                    entry = self._getNext(iterObj)
                    continue
                
                # both are valid
                EntryVal = entry.getCourse() if entry else None
                CmpValue = CmpEntry.getCourse() if CmpEntry else None
               
                # comparing class
                if entry.getClass() > CmpEntry.getClass():
                    Html += self._GenerateTableEntries(WeekNo, None, CmpEntry )
                    CmpEntry = self._getNext(iterCmpObj)                
                    continue
                if entry.getClass() < CmpEntry.getClass():
                    Html += self._GenerateTableEntries(WeekNo, entry, None )
                    entry = self._getNext(iterObj)
                    continue

                # comparing course
                if EntryVal < CmpValue:
                    Html += self._GenerateTableEntries(WeekNo, entry, None )
                    entry = self._getNext(iterObj)
                    continue
                if (EntryVal > CmpValue):
                    Html += self._GenerateTableEntries(WeekNo, None, CmpEntry )
                    CmpEntry = self._getNext(iterCmpObj)                
                    continue
                if EntryVal == CmpValue:
                    Html += self._GenerateTableEntries(WeekNo, entry, CmpEntry )
                    entry = self._getNext(iterObj)
                    CmpEntry = self._getNext(iterCmpObj)
                    continue

                raise ValueError("Should never get here!")
        else:
            while( entry ):        
                Html += self._GenerateTableEntries(WeekNo, entry, None )
                entry = self._getNext(iterObj)
                
        Html += "\t</table>\n"
        return Html
    
    def _getNext(self, iter ):
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
        if not entry:
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( None, CmpEntry.getClass() )
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( None, CmpEntry.getTeacher() )
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( None, CmpEntry.getCourse() )
        elif not CmpEntry:
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( entry.getClass(), None )
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( entry.getTeacher(), None )
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( entry.getCourse(), None )
        else:
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( entry.getClass(), CmpEntry.getClass() )
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( entry.getTeacher(), CmpEntry.getTeacher() )
            TTable += "\t\t\t<td>%s</td>\n" % self._CellContent( entry.getCourse(), CmpEntry.getCourse() )
            
        # the weeks
        for Week in WeekNo:
            if not entry:
                Content = self._CellContent( None, CmpEntry.getLessons(Week) ) 
            elif not CmpEntry:
                Content = self._CellContent( entry.getLessons(Week), None ) 
            else:
                Content = self._CellContent( entry.getLessons(Week), CmpEntry.getLessons(Week) ) 

            TTable += "\t\t\t<td>%s</td>\n" % Content

        TTable += "\t\t</tr>\n"
        return TTable

    def _CellContent(self, EntryTxt, CmpEntryTxt ):
        # the case of no lesson in week
        if (not EntryTxt) and (not CmpEntryTxt):
            return ""
         
        if not self._CmpObj:
            return EntryTxt if EntryTxt else ""
        
        txt = "<table class=\"%s\">" % (self._CssClassEqual if EntryTxt == CmpEntryTxt else self._CssClassDiff )
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

