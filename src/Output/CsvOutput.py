'''
Created on Aug 12, 2012

@author: moz
'''

from datetime import date, timedelta
from operator import itemgetter

def _CreateSumRow(RowSums, Header, ColumnSums):
    SumRowSum = 0
    HtmlTable = "\t<tr>"
    for entry in Header: #@UnusedVariable
        HtmlTable += "<td></td>"
    
    for weekno in sorted(ColumnSums.keys()):
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
        WeekDate = date(Week['Year'] - 1, 12, 31) + timedelta(7 * Week['Week'])
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

def CsvOutput( Weeksums, Headers = ["Class", "Subject"] ):
    ''' No filtering or sorting is done. Data is dumped as supplied '''
        
    WeekRange, Data = _PreprocessData(Weeksums)

    if not WeekRange:
        return "No data"

    # output header line
    # TODO: Header = ("Class", "Teacher", "Course")
    #Header = ("Class", "Subject")
    
    CsvList = []

    # header output
    HeaderList = []
    for text in Headers:
        HeaderList.append( text )

    # output weeks in header row.
    ColumnSums = {}
    CurWeek = WeekRange[0]
    #CurWeek = datetime.datetime.strptime(WeekRange[0], "%Y-%m-%d" ).date()
    #print(CurWeek)
    #while CurWeek <= datetime.datetime.strptime(WeekRange[1], "%Y-%m-%d" ).date():
    while CurWeek <= WeekRange[1]:
        Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
        HeaderList.append( u"%d-%d"%(Year, Week) )
        ColumnSums[str(Year)+str(Week)] = 0
        CurWeek += timedelta(7) # add 7 days
    
    CsvList.append( HeaderList )


    # output content
    LastEntry = ""
    CurRowSum = 0
    CurList = []
    
    for CurEntry in Data:
        for Id in Headers:
            try:
                if CurEntry[Id] == LastEntry[Id]:
                    continue
            except:
                pass
            
            if LastEntry != "":
                # end row
                while CurWeek <= WeekRange[1]:
                    CurList.append( u'.' )
                    CurWeek += timedelta(7)
                
                CsvList.append( CurList )
        
            # new row
            CurRowSum = 0
            #CurWeek = datetime.datetime.strptime(WeekRange[0], "%Y-%m-%d" ).date()
            CurWeek = WeekRange[0]
            CurList = []
            
            # output class and subject
            for text in Headers:
                CurList.append( CurEntry[text] )
            
            break
    
        # loop through the week of current class+subject combination (the DataStr from above)
        #while CurWeek <= datetime.datetime.strptime(WeekRange[1], "%Y-%m-%d" ).date():
        while CurWeek <= WeekRange[1]:
            Year, Week, Weekday = CurWeek.isocalendar() #@UnusedVariable
            #if (datetime.datetime.strptime(CurEntry['Week'], "%Y-%m-%d" ).date() == CurWeek):
            if (CurEntry['Week'] == Week):
                CurList.append( CurEntry['LessonCount'] )
                #todo: remove Year form weeksums entries - it is no longer needed since weeks are based on date of mondays
                # updating row sums
                CurRowSum += CurEntry['LessonCount']

                # updating column sums
                ColumnSums[str(Year)+str(Week)] += CurEntry['LessonCount']
                
                LastEntry = CurEntry
                CurWeek += timedelta(7) # add 7 days

                break
            else:
                CurList.append( u'.' )
            CurWeek += timedelta(7) # add 7 days
    
    # this loop will add empty spaced to the last subject
    #while CurWeek <= datetime.datetime.strptime(WeekRange[1], "%Y-%m-%d" ).date():
    while CurWeek <= WeekRange[1]:
        CurList.append( u'.' )
        CurWeek += timedelta(7) # add 7 days
        
    # end row
    CsvList.append( CurList )
    
    return CsvList

