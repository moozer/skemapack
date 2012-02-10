'''
Created on 10 Feb 2012

@author: moz
'''
from datetime import time, date, datetime, timedelta

def HtmlTableOutput( Weeksums ):
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
    #Header = ("Class", "Teacher", "Course")
    Header = ("Class", "Subject")
    
    # table start
    HtmlTable = "<table>\n"
    
    # header output
    HtmlTable += "\t<tr>"
    for text in Header:
        HtmlTable += "<td>%s</td>"%text

    CurWeek = WeekRange[0]
    while CurWeek <= WeekRange[1]:
        Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
        HtmlTable += "<td>%d-%d</td>"%(Year, Week)        
        CurWeek += timedelta(7) # add 7 days
    
    HtmlTable += "</tr>\n"
    
    # output content
    for Entry in Data.keys():
        CurEntry = Data[Entry]
        
        HtmlTable += "\t<tr>"
        for text in Header:
            HtmlTable += "<td>%s</td>"%CurEntry[0][text]
    
        CurWeek = WeekRange[0]
        EntryCounter = 0
        while CurWeek <= WeekRange[1]:
            Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
            if      (CurEntry[EntryCounter]['Year'] == Year) \
                and (CurEntry[EntryCounter]['Week'] == Week):
                HtmlTable += "<td>%d</td>"%CurEntry[EntryCounter]['LessonCount']
                EntryCounter += 1
            else:
                HtmlTable += "<td>.</td>"
            CurWeek += timedelta(7) # add 7 days
        
        HtmlTable += "</tr>\n"
    
    # table end    
    HtmlTable += "</table>\n"
    
    return HtmlTable


