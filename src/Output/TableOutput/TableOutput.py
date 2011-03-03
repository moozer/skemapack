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

    def __init__(self, ItObject, IncludeHeader=True, 
                 IncludeColumnSums = False, IncludeRowSums = False, IncludePreperation=False,
                 ItObjectExtra = None ):
        '''
        Constructor
        @param param: ItObject An proper iterable object with values in lessons
        @param param: ItObjectExtra An proper iterable object with values in hours
        '''
        self._ItObject = ItObject
        self._ItObjectExtra = ItObjectExtra
        self._HeaderElements = ['Class','Teacher', 'Course']
        self._WeeklistKey = 'Lessons by week'
        self._TextileTable = ""
        self._IncludeHeader = IncludeHeader
        self._IncludeColumnSums = IncludeColumnSums
        self._IncludeRowSums = IncludeRowSums
        self._IncludePreperation = IncludePreperation
        self._WeekNo = []

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


    def _GenerateColumnSumsLine(self, ColumnSums, WeekNo, IncludeRowSums ):
        ''' Generates the bottom line with the sums of lessons
        @param WeekNo: The list of weeks to include 
        @param ColumnSums: The dictionary which holds the sums.
        @param IncludeRowSums: If true, an extra cell with the global sum is included
        @return: the table text for the header part.
        ''' 
        TTable = ""
        Sum = 0

        TTable += "| Sum "
        for i in range( 2, len(self._HeaderElements)+1):
            TTable += "|"
        
        for Week in WeekNo:
            TTable += "|"
            if str(Week) in ColumnSums:
                Sum += ColumnSums[str(Week)]
                TTable += str(ColumnSums[str(Week)])
        if IncludeRowSums:
            TTable += "|"+"{0: .1f}".format(Sum)
            
        TTable += "|\n"
        return TTable
    

    def _GenerateColumnSumsHours(self, ColumnSums, WeekNo ):
        ''' Generates the bottom line with the sums in hours + prep
        @param WeekNo: The list of weeks to include 
        @param ColumnSums: The dictionary which holds the sums.
        @return: the table text for the header part.
        ''' 
        Hours = {}
        Prep = {}
        HourTotal = {}
        for Week in WeekNo:
            if str(Week) in ColumnSums:
                Hours[str(Week)] = ColumnSums[str(Week)]*0.75
                for prevWeek in range(Week-6, Week):
                    Prep[str(prevWeek)] = ColumnSums[str(Week)]*0.175 + Prep.get(str(prevWeek),0)
                    # TODO: fix hardcoded values (108 min - 45)/6
                    
        
        TTable = ""
        if self._IncludeColumnSums:
            TTable += "| Lessons (hours) "
            for i in range( 2, len(self._HeaderElements)+1):
                TTable += "|"
            #for e in self._HeaderElements: #@UnusedVariable
            #    TTable += "|"
            
            RowSum = 0
            for Week in WeekNo:
                TTable += "|"
                if str(Week) in Hours:
                    RowSum += Hours[str(Week)]
                    TTable += str(Hours[str(Week)])
            
            # add the sum cell if applicable
            if self._IncludeRowSums:
                TTable += "|" + str(RowSum)
            
            TTable += "|\n"
            
        if self._IncludePreperation:
            TTable += "| Preparation "
            for i in range( 2, len(self._HeaderElements)+1):
                TTable += "|"
            #for e in self._HeaderElements: #@UnusedVariable
            #    TTable += "|"
            
            RowSum = 0
            for Week in WeekNo:
                TTable += "|"
                if str(Week) in Prep:
                    RowSum += Prep.get(str(Week),"")
                    TTable += "{0: .1f}".format(Prep.get(str(Week),""))

            # add the sum cell if applicable
            if self._IncludeRowSums:
                TTable += "|" + str(RowSum)
            
            
            TTable += "|\n"
            
        # update column sums for later use
        for Week in WeekNo:
            if str(Week) in Prep:
                ColumnSums[str(Week)] = Prep.get(str(Week),0)+Hours.get(str(Week),0)
            elif Hours.get(str(Week),0) > 0:
                ColumnSums[str(Week)] = Hours.get(str(Week),0)
        #=======================================================================
        # if self._IncludePreperation:
        #    for e in self._HeaderElements: #@UnusedVariable
        #        TTable += "|"
        #    
        #    for Week in WeekNo:
        #        TTable += "|"
        #        if str(Week) in Prep:
        #            TTable += "{0: .0f}".format((Prep.get(str(Week),0)+Hours.get(str(Week),0)))
        #    
        #    TTable += "|\n"
        #=======================================================================
                
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

    def _GenerateExtraTableEntries(self, ColumnSums, WeekNo, entry, IncludeRowSums):
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
        if self._IncludePreperation:
            WeekNo = range(StartWeek-6, EndWeek+1) # TODO: 6 is the number of weeks for preparations
        else:
            WeekNo = range(StartWeek, EndWeek+1)
            
        for entry in self._ItObject:
            # first entry to be used for header titles (course, teacher etc)
            if FirstEntry:
                    
                if self._IncludeHeader:
                    TTable += self._GenerateHeader(WeekNo, entry, self._IncludeRowSums)
                    
                FirstEntry = False
                
            # other entries
            TTable += self._GenerateTableEntries(ColumnSums, WeekNo, entry, self._IncludeRowSums)
        
        # append column sums.
        if self._IncludeColumnSums:
            TTable += self._GenerateColumnSumsLine(ColumnSums, WeekNo, self._IncludeRowSums)      
                    
        # append column sums measured in hours + prep.
        if self._IncludePreperation:
            TTable += self._GenerateColumnSumsHours(ColumnSums, WeekNo)             
        
        # append extra stuff
        if self._ItObjectExtra:
            for entry in self._ItObjectExtra:
                TTable += self._GenerateExtraTableEntries(ColumnSums, WeekNo, entry, self._IncludeRowSums)

        # append column sums.
        if self._IncludeColumnSums:
            TTable += self._GenerateColumnSumsLine(ColumnSums, WeekNo, self._IncludeRowSums)      

        self._WeekNo = WeekNo
        self._TextileTable = TTable
        return TTable

    def GetHtmlTable(self, StartWeek=38, EndWeek=52):
        ''' Converts the textile to html '''
        self.GetTextileTable( StartWeek, EndWeek)
        result = textile.textile( self._TextileTable)
        return result
    
    def GetWeeks(self):
        ''' returns the resulting week used in html generation '''
        return self._WeekNo    