'''
Created on Nov 14, 2010

@author: morten
'''
import unittest
from Input.HtmlScraper.DalumSkemaScraper import DalumSkemaScraper

# test data
DalumDataFile = "Dalum/Merete_2010_35.htm"
DalumData = open(DalumDataFile, 'r').read()
DalumDataAppCount = 21

class Test(unittest.TestCase):

    def testConstructor(self):
        ''' Test construction of dalum scraper '''
        s = DalumSkemaScraper( 1427 )
        self.assertEqual( s.GetId(), 1427)
        self.assertEqual( s.IsSourceWeb(), True )

    def testSetSource(self):
        ''' Test get/set html'''
        s = DalumSkemaScraper( 1427 )
        s.SetHtml( DalumData )
        self.assertEqual( s.IsSourceWeb(), False)
        self.assertEqual( s.GetHtml(),DalumData )

    def testExtractAppointmentsFromHtml(self):
        ''' Extract the appointments from the tests data file '''
        s = DalumSkemaScraper( 1427 )
        s.SetHtml( DalumData )
        self.assertEqual( s.ExtractAppointments(), DalumDataAppCount )

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConstructor']
    unittest.main()