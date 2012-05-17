'''
Created on 10 Feb 2012

@author: moz
'''
from datetime import date, timedelta
from operator import itemgetter
import datetime

def _CreateSumRow(RowSums, Header, ColumnSums):
    SumRowSum = 0
    HtmlTable = "\t<tr>"
    for entry in Header: #@UnusedVariable
        HtmlTable += "<td></td>"
    
    for weekno in ColumnSums.keys():
        if ColumnSums[weekno] == 0:
            HtmlTable += "<td>.</td>"
        else:
            HtmlTable += "<td>%d</td>" % ColumnSums[weekno]
        # calculating the sum of columns also
        SumRowSum += ColumnSums[weekno]
    
    if RowSums:
        HtmlTable += "<td>%d</td>" % SumRowSum
    HtmlTable += "</tr>\n"
    
    return HtmlTable


def _PreprocessData(Weeksums):
    ''' Extracts weekrange and sorts '''
    WeekRange = None
    Data = {}
    for Week in Weeksums: # get the range for week in data
        # dec 31th is never week 1. jan 1st might be.
        #WeekDate = date(Week['Year'] - 1, 12, 31) + timedelta(7 * Week['Week'])
        WeekDate = Week['Week']
        if not WeekRange:
            WeekRange = [WeekDate, WeekDate]
        if WeekDate > WeekRange[1]:
            WeekRange[1] = WeekDate
        if WeekDate < WeekRange[0]:
            WeekRange[0] = WeekDate
        # process for same Class-Subject combo.
        DataStr = Week['Class'], Week['Subject']
        if not DataStr in Data.keys():
            Data[DataStr] = []
        Data[DataStr].append(Week)
    
    SortedData = sorted( Weeksums, key=itemgetter("Class", "Subject", "Year", "Week") )
    
    return WeekRange, SortedData

def HtmlTableOutput( Weeksums, RowSums = False, ColSums = False, Headers = ["Class", "Subject"] ):
    ''' No filtering or sorting is done. Data is dumped as supplied '''
        
    WeekRange, Data = _PreprocessData(Weeksums)

    # output header line
    # TODO: Header = ("Class", "Teacher", "Course")
    #Header = ("Class", "Subject")
    
    # table start
    HtmlTable = "<table>\n"
    
    # header output
    HtmlTable += "\t<tr>"
    for text in Headers:
        HtmlTable += "<td>%s</td>"%text

    # output weeks in header row.
    ColumnSums = {}
    #CurWeek = WeekRange[0]
    CurWeek = datetime.datetime.strptime(WeekRange[0], "%Y-%m-%d" ).date()
    #print(CurWeek)
    while CurWeek <= datetime.datetime.strptime(WeekRange[1], "%Y-%m-%d" ).date():
        Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
        HtmlTable += "<td class=\"WeekHeader\">%d-%d</td>"%(Year, Week)
        ColumnSums[Week] = 0
        CurWeek += timedelta(7) # add 7 days
    
    # Row sums, if applicable
    if RowSums:
        HtmlTable += "<td>Sum</td>"
    
    HtmlTable += "</tr>\n"

    # output content
    LastEntry = ""
    CurRowSum = 0

    for CurEntry in Data:
        
        for Id in Headers:
            try:
                if CurEntry[Id] == LastEntry[Id]:
                    continue
            except:
                pass
            
            if LastEntry != "":
                # end row
                while CurWeek <= datetime.datetime.strptime(WeekRange[1], "%Y-%m-%d" ).date():
                    HtmlTable += "<td>.</td>"
                    CurWeek += timedelta(7)
                
                if RowSums:
                    HtmlTable += "<td>%d</td>"%CurRowSum
                HtmlTable += "</tr>\n"
        
            # new row
            CurRowSum = 0
            CurWeek = datetime.datetime.strptime(WeekRange[0], "%Y-%m-%d" ).date()
            HtmlTable += "\t<tr>"
            
            # output class and subject
            for text in Headers:
                HtmlTable += "<td>%s</td>"%CurEntry[text]
            
            break
    
        # loop through the week of current class+subject combination (the DataStr from above)
        while CurWeek <= datetime.datetime.strptime(WeekRange[1], "%Y-%m-%d" ).date():
            Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
            if      (CurEntry['Year'] == Year) \
                and (datetime.datetime.strptime(CurEntry['Week'], "%Y-%m-%d" ).date() == CurWeek):
                HtmlTable += "<td>%d</td>"%CurEntry['LessonCount']
            
                # updating row sums
                CurRowSum += CurEntry['LessonCount']

                # updating column sums
                ColumnSums[Week] += CurEntry['LessonCount']
                
                LastEntry = CurEntry
                CurWeek += timedelta(7) # add 7 days

                break
            else:
                HtmlTable += "<td>.</td>"
            CurWeek += timedelta(7) # add 7 days
        
    # end row
    if RowSums:
        HtmlTable += "<td>%d</td>"%CurRowSum
    HtmlTable += "</tr>\n"

    # append row with column sums    
    if ColSums:
        HtmlTable += _CreateSumRow(RowSums, Headers, ColumnSums)

    # table end    
    HtmlTable += "</table>\n"
    
    return HtmlTable


