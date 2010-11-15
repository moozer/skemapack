'''
Created on Nov 14, 2010

@author: morten
'''
import unittest, datetime
from Input.HtmlScraper.DalumSkemaScraper import DalumSkemaScraper

# test data
DalumDataFile = "Dalum/Merete_2010_35.htm"
DalumId = 1427
DalumWeek = 35
DalumData = open(DalumDataFile, 'r').read()
DalumDataAppCount = 21
DalumDataDates = {   'Monday': datetime.datetime(2010, 8, 30, 0, 0),
    'Tuesday': datetime.datetime(2010, 8, 31, 0, 0), 
    'Wednesday': datetime.datetime(2010, 9, 1, 0, 0), 
    'Thursday': datetime.datetime(2010, 9, 2, 0, 0), 
    'Friday': datetime.datetime(2010, 9, 3, 0, 0) }

DalumDataAppointment = [   
    {'Date': datetime.datetime(2010, 8, 31, 0, 0), 'Hours': [datetime.datetime(2010, 8, 31, 9, 5), datetime.datetime(2010, 8, 31, 9, 50)], 'Location': u'F5F6', 'Class': u'J1F5J1F6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 8, 31, 0, 0), 'Hours': [datetime.datetime(2010, 8, 31, 10, 10), datetime.datetime(2010, 8, 31, 10, 55)], 'Location': u'F5F6', 'Class': u'J1F5J1F6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 8, 31, 0, 0), 'Hours': [datetime.datetime(2010, 8, 31, 11, 0), datetime.datetime(2010, 8, 31, 11, 45)], 'Location': u'F5F6', 'Class': u'J1F5J1F6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 8, 31, 0, 0), 'Hours': [datetime.datetime(2010, 8, 31, 12, 30), datetime.datetime(2010, 8, 31, 13, 15)], 'Location': u'F5F6', 'Class': u'J1F5J1F6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 8, 31, 0, 0), 'Hours': [datetime.datetime(2010, 8, 31, 13, 20), datetime.datetime(2010, 8, 31, 14, 5)], 'Location': u'F5F6', 'Class': u'J1F5J1F6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 8, 31, 0, 0), 'Hours': [datetime.datetime(2010, 8, 31, 14, 25), datetime.datetime(2010, 8, 31, 15, 10)], 'Location': u'F5F6', 'Class': u'J1F5J1F6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 8, 31, 0, 0), 'Hours': [datetime.datetime(2010, 8, 31, 15, 15), datetime.datetime(2010, 8, 31, 16, 0)], 'Location': u'F5F6', 'Class': u'J1F5J1F6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 9, 1, 0, 0), 'Hours': [datetime.datetime(2010, 9, 1, 12, 30), datetime.datetime(2010, 9, 1, 13, 15)], 'Location': u'D6', 'Class': u'JHD6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 9, 1, 0, 0), 'Hours': [datetime.datetime(2010, 9, 1, 13, 20), datetime.datetime(2010, 9, 1, 14, 5)], 'Location': u'D6', 'Class': u'JHD6', 'Subject': u'Introduktion'}, 
    {'Date': datetime.datetime(2010, 9, 1, 0, 0), 'Hours': [datetime.datetime(2010, 9, 1, 14, 25), datetime.datetime(2010, 9, 1, 15, 10)], 'Location': u'D6', 'Class': u'JHD6', 'Subject': u'HU/PL speciale'}, 
    {'Date': datetime.datetime(2010, 9, 1, 0, 0), 'Hours': [datetime.datetime(2010, 9, 1, 15, 15), datetime.datetime(2010, 9, 1, 16, 0)], 'Location': u'D6', 'Class': u'JHD6', 'Subject': u'HU/PL speciale'}, 
    {'Date': datetime.datetime(2010, 9, 2, 0, 0), 'Hours': [datetime.datetime(2010, 9, 2, 8, 15), datetime.datetime(2010, 9, 2, 9, 0)], 'Location': u'F6', 'Class': u'J1F6', 'Subject': u'EDB'}, 
    {'Date': datetime.datetime(2010, 9, 2, 0, 0), 'Hours': [datetime.datetime(2010, 9, 2, 9, 5), datetime.datetime(2010, 9, 2, 9, 50)], 'Location': u'F5', 'Class': u'J1F5', 'Subject': u'EDB'}, 
    {'Date': datetime.datetime(2010, 9, 2, 0, 0), 'Hours': [datetime.datetime(2010, 9, 2, 12, 30), datetime.datetime(2010, 9, 2, 13, 15)], 'Location': u'KE', 'Class': u'GRFE', 'Subject': u'Husdyrbiologi'}, 
    {'Date': datetime.datetime(2010, 9, 2, 0, 0), 'Hours': [datetime.datetime(2010, 9, 2, 13, 20), datetime.datetime(2010, 9, 2, 14, 5)], 'Location': u'KE', 'Class': u'GRFE', 'Subject': u'Husdyrbiologi'}, 
    {'Date': datetime.datetime(2010, 9, 2, 0, 0), 'Hours': [datetime.datetime(2010, 9, 2, 14, 25), datetime.datetime(2010, 9, 2, 15, 10)], 'Location': u'KD', 'Class': u'GRFD', 'Subject': u'Husdyrbiologi'}, 
    {'Date': datetime.datetime(2010, 9, 2, 0, 0), 'Hours': [datetime.datetime(2010, 9, 2, 15, 15), datetime.datetime(2010, 9, 2, 16, 0)], 'Location': u'KD', 'Class': u'GRFD', 'Subject': u'Husdyrbiologi'}, 
    {'Date': datetime.datetime(2010, 9, 3, 0, 0), 'Hours': [datetime.datetime(2010, 9, 3, 8, 15), datetime.datetime(2010, 9, 3, 9, 0)], 'Location': u'KD', 'Class': u'GRFD', 'Subject': u'Husdyrbiologi'}, 
    {'Date': datetime.datetime(2010, 9, 3, 0, 0), 'Hours': [datetime.datetime(2010, 9, 3, 9, 5), datetime.datetime(2010, 9, 3, 9, 50)], 'Location': u'KD', 'Class': u'GRFD', 'Subject': u'Husdyrbiologi'}, 
    {'Date': datetime.datetime(2010, 9, 3, 0, 0), 'Hours': [datetime.datetime(2010, 9, 3, 10, 10), datetime.datetime(2010, 9, 3, 10, 55)], 'Location': u'KE', 'Class': u'GRFE', 'Subject': u'Husdyrbiologi'}, 
    {'Date': datetime.datetime(2010, 9, 3, 0, 0), 'Hours': [datetime.datetime(2010, 9, 3, 11, 0), datetime.datetime(2010, 9, 3, 11, 45)], 'Location': u'KE', 'Class': u'GRFE', 'Subject': u'Husdyrbiologi'}] 

DalumUrl = "http://80.208.123.243/uge%2035/"

class Test(unittest.TestCase):

    def testConstructor(self):
        ''' DalumSkemaScraper : Test construction of dalum scraper '''
        s = DalumSkemaScraper( DalumId )
        self.assertEqual( s.GetId(), DalumId)
        self.assertEqual( s.IsSourceWeb(), True )

    def testSetSource(self):
        ''' DalumSkemaScraper : Test get/set html'''
        s = DalumSkemaScraper( DalumId )
        s.SetHtml( DalumData )
        self.assertEqual( s.IsSourceWeb(), False)
        self.assertEqual( s.GetHtml(),DalumData )

    def testExtractAppointmentsFromHtml(self):
        ''' DalumSkemaScraper : Extract the appointments from the tests data file '''
        s = DalumSkemaScraper( DalumId )
        s.SetHtml( DalumData )
        s.ExtractAppointments()
        self.assertEqual( s.GetDates(), DalumDataDates )
        self.assertEqual( s.ExtractAppointments(), DalumDataAppCount )
        self.assertEqual( s.GetAppointments(), DalumDataAppointment)

    def testGetFromWebWithoutWeek(self):
        ''' DalumSkemaScraper : test failure to retrieve html from internet '''
        s = DalumSkemaScraper( DalumId  )
        self.assertRaises( ValueError, s.ExtractAppointments )
                
    def testGetFromWebWithBadWeek(self):
        ''' DalumSkemaScraper : test failure to process bad html from internet '''
        BadWeekNo = 100
        s = DalumSkemaScraper( DalumId, [BadWeekNo]  )
        self.assertRaises( ValueError, s.ExtractAppointments )
                
    def testGetFromWeb(self):
        ''' DalumSkemaScraper : test correct retrieval of html from internet '''
        s = DalumSkemaScraper( DalumId, [DalumWeek]  )
        s.ExtractAppointments()
        self.assertEqual( s.GetDates(), DalumDataDates )
        self.assertEqual( s.ExtractAppointments(), DalumDataAppCount )
        self.assertEqual( s.GetAppointments(), DalumDataAppointment)
        
#    def testGetMultiWeekFromWeb(self):
#        ''' DalumSkemaScraper : test correct retrieval of html from internet '''
#        s = DalumSkemaScraper( DalumId, [DalumWeek, DalumWeek+1]  )
#        s.ExtractAppointments()
#        self.assertEqual( s.GetDates(), DalumDataDates )
#        self.assertEqual( s.ExtractAppointments(), DalumDataAppCount )
#        self.assertEqual( s.GetAppointments(), DalumDataAppointment)
                 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConstructor']
    unittest.main()