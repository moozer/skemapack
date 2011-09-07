'''
Created on Sep 7, 2011

@author: morten
'''
import unittest

from Input.HtmlScraper.SdeSkema import SdeSkema
from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
from TestSdeSkemaScraper import SimpleSkemaData

class Test(unittest.TestCase):


    def testSdeSkemaIterator(self):
        """ SdeSkemaScraper : test iterator functionality """
        parser = SdeSkemaScraper()
        parser.feed(SimpleSkemaData)
        parser.close()
        
        i = 0
        for entry in SdeSkema( SimpleSkemaData ):
            self.assertEqual( entry, parser.Appointments[i] )
            i = i+1
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()