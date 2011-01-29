# -*- coding: UTF-8 -*-

'''
Created on Oct 12, 2010

@author: pfl
'''
import unittest, datetime
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper

# variables
Filename_pfl_2011_04 = "testPage_pfl_2011_04.html"

class Test(unittest.TestCase):

    def testGetSkemaWithPost_1(self):
        ''' HtmlGetter : do a POST 1 week'''
        myLoader = loadWeb.htmlGetter()
        try:
            self._htmlResponse = myLoader.getSkemaWithPost(3735, 43, 43, 2010)
        except IOError:
            self.fail("IOError. No internet?")
        parser = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( self._htmlResponse.read() )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,19)
        pass
    
    def testGetSkemaWithPost_2(self):
        ''' HtmlGetter : do a POST 5 weeks '''
        # TODO : can we change this into a static test? As it is now it requires net-access and fails if changes are made
        myLoader = loadWeb.htmlGetter()
        try:
            self._htmlResponse = myLoader.getSkemaWithPost(3735, 43, 48, 2010)
        except IOError:
            self.fail("IOError. No internet?")
        parser = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( self._htmlResponse.read() )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,75)
        pass

    def testGetSkemaWithPostWithSpecifiedYear(self):
        ''' HtmlGetter : do a POST 1 week with the year specified'''
        myLoader = loadWeb.htmlGetter()
        try:
            self._htmlResponse = myLoader.getSkemaWithPost(3735, 04, 04, 2011)
        except IOError:
            self.fail("IOError. No internet?")
        parser = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( self._htmlResponse.read() )
        parser.close()
        
        fp = open( Filename_pfl_2011_04, "r" )
        Filecontent = fp.read()
        fp.close()
        parser2 = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser2.feed( Filecontent )
        parser2.close()
        
        self.assertEqual(parser.Appointments, parser2.Appointments)
        pass

    def testGetGetterParameters(self):
        ''' HtmlGetter : checks if the current year is chosen, if no year is supplied '''
        UserId = 3735
        StartWeek = 04
        EndWeek = 04
        Year = datetime.datetime.now().year
        ExpectedParams = {'id': UserId, 'startWeek': StartWeek, 'endWeek': EndWeek, 'year': Year}

        myLoader = loadWeb.htmlGetter()
        try:
            myLoader.getSkemaWithPost(3735, 04, 04)
        except IOError:
            self.fail("IOError. No internet?")
            
        Params = myLoader.getParameters()
        self.assertEqual(ExpectedParams, Params )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()