'''
Created on May 27, 2011

@author: morten
'''

class HtmlOutput():
    '''
    classdocs
    '''


    def __init__(self, ItObj):
        '''
        Constructor
        '''
        self._ItObject = ItObj
        self._HeaderElements = ['Class','Teacher', 'Course']
        
    def GetHtmlTable(self, StartWeek=38, EndWeek=52 ):
        ''' Loops through the data and builds the html table '''
        Html = "\t<table>\n"
        FirstEntry = True

        WeekNo = range(StartWeek, EndWeek+1)

        for entry in self._ItObject:
            # first entry to be used for header titles (course, teacher etc)
            if FirstEntry:
                Html += self._GenerateHeader(WeekNo, entry )                    
                FirstEntry = False
                
            # other entries
            Html += self._GenerateTableEntries(WeekNo, entry)
        
        Html += "\t</table>\n"
        return Html
    
    def _GenerateTableEntries(self, WeekNo, entry):
        ''' Generates the lines with the course info
        @param WeekNo: The list of weeks to include 
        @param entry: the course entry
        @return: the table text for the header part.
        ''' 
        TTable = "\t\t<tr>\n"
        RowSum = 0
        
        # Course name, teacher name, etc.
        TTable += "\t\t\t<td>%s</td>\n" % entry.getClass()
        TTable += "\t\t\t<td>%s</td>\n" % entry.getTeacher()
        TTable += "\t\t\t<td>%s</td>\n" % entry.getCourse()

        # the weeks
        for Week in WeekNo:
            if Week in entry.getListOfWeeks():
                TTable += "\t\t\t<td>%s</td>\n" % str(entry.getLessons( Week ) )
            else:
                TTable += "\t\t\t<td></td>\n"

        TTable += "\t\t</tr>\n"
        return TTable

    def _GenerateHeader(self, WeekNo, entry ):
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

