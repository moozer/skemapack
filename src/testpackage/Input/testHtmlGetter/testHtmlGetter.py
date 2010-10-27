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
        self._htmlResponse = myLoader.getSkemaWithPost(3735, 43, 43)
        parser = BeautifulSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( self._htmlResponse.read() )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,19)
        pass
    
    def testGetSkemaWithPost_2(self):
        ''' HtmlGetter : do a POST 5 weeks '''
        myLoader = loadWeb.htmlGetter()
        self._htmlResponse = myLoader.getSkemaWithPost(3735, 45, 45)
        parser = BeautifulSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( self._htmlResponse.read() )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,72)
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()