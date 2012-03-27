'''
Created on 10 Feb 2012

@author: moz
'''
from datetime import date, timedelta

def HtmlTableOutput( Weeksums, RowSums = False, ColSums = False ):
    ''' No filtering or sorting is done. Data is dumped as supplied '''
        
    WeekRange = None
    Data = {}
    for Week in Weeksums:
        # get the range for week in data
        # dec 31th is never week 1. jan 1st might be.
        WeekDate = date( Week['Year']-1, 12, 31) + timedelta( 7 * Week['Week'] )
        if not WeekRange:
            WeekRange = [WeekDate, WeekDate]
        
        if WeekDate > WeekRange[1]:
            WeekRange[1] = WeekDate
        if WeekDate < WeekRange[0]:
            WeekRange[0] = WeekDate
            
        # process for same Class-Subject combo.
        DataStr = "%s-%s"%(Week['Class'], Week['Subject'])
        if not DataStr in Data.keys():
            Data[DataStr] = []
            
        Data[DataStr].append(Week)

    # output header line
    # TODO: Header = ("Class", "Teacher", "Course")
    Header = ("Class", "Subject")
    
    # table start
    HtmlTable = "<table>\n"
    
    # header output
    HtmlTable += "\t<tr>"
    for text in Header:
        HtmlTable += "<td>%s</td>"%text

    # output weeks in header row.
    ColumnSums = {}
    CurWeek = WeekRange[0]
    while CurWeek <= WeekRange[1]:
        Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
        HtmlTable += "<td>%d-%d</td>"%(Year, Week)
        ColumnSums[Week] = 0
        CurWeek += timedelta(7) # add 7 days
    
    # Row sums, if applicable
    if RowSums:
        HtmlTable += "<td>Sum</td>"
    
    HtmlTable += "</tr>\n"

    # output content
    for Entry in Data.keys():
        CurEntry = Data[Entry]
        
        # new row
        CurRowSum = 0
        HtmlTable += "\t<tr>"
        
        # output class and subject
        for text in Header:
            HtmlTable += "<td>%s</td>"%CurEntry[0][text]
    
        # loop through the week of current class+subject combination (the DataStr from above)
        CurWeek = WeekRange[0]
        EntryCounter = 0
        while CurWeek <= WeekRange[1]:
            # are we looking at a week of the last of current lessons?
            if EntryCounter >= len(CurEntry):
                HtmlTable += "<td>.</td>"
                CurWeek += timedelta(7) # add 7 days
                continue
            
            Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
            if      (CurEntry[EntryCounter]['Year'] == Year) \
                and (CurEntry[EntryCounter]['Week'] == Week):
                HtmlTable += "<td>%d</td>"%CurEntry[EntryCounter]['LessonCount']
                
                # updating row sums
                CurRowSum += CurEntry[EntryCounter]['LessonCount']

                # updating column sums
                ColumnSums[Week] += CurEntry[EntryCounter]['LessonCount']

                EntryCounter += 1
            else:
                HtmlTable += "<td>.</td>"
            CurWeek += timedelta(7) # add 7 days
        
        # end row
        if RowSums:
            HtmlTable += "<td>%d</td>"%CurRowSum
        HtmlTable += "</tr>\n"

    # append row with clumn sums    
    if ColSums:
        
        SumRowSum = 0
        
        HtmlTable += "\t<tr>"        
        for entry in Header: #@UnusedVariable
            HtmlTable += "<td></td>"
            
        for weekno in ColumnSums.keys():
            if ColumnSums[weekno] == 0:
                HtmlTable += "<td>.</td>"                
            else:
                HtmlTable += "<td>%d</td>"%ColumnSums[weekno]
            
            # calculating the sum of columns also
            SumRowSum += ColumnSums[weekno]
            
        if RowSums:
            HtmlTable += "<td>%d</td>"%SumRowSum
            
        
        HtmlTable += "</tr>\n"

    # table end    
    HtmlTable += "</table>\n"
    
    return HtmlTable


