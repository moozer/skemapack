# -*- coding: UTF-8 -*-

'''
Created on Oct 12, 2010

@author: pfl
'''
import unittest
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb
from Input.HtmlScraper.BeautifulSkemaScraper import  BeautifulSkemaScraper

class Test(unittest.TestCase):

    def testGetSkemaWithPost_1(self):
        ''' HtmlGetter : do a POST 1 week'''
        myLoader = loadWeb.htmlGetter()
        try:
            self._htmlResponse = myLoader.getSkemaWithPost(3735, 43, 43)
        except IOError:
            self.fail("IOError. No internet?")
        parser = BeautifulSkemaScraper(DateFormat = "%d-%m-%Y")
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
            self._htmlResponse = myLoader.getSkemaWithPost(3735, 43, 48)
        except IOError:
            self.fail("IOError. No internet?")
        parser = BeautifulSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( self._htmlResponse.read() )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,75)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()