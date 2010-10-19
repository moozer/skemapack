'''
Created on Oct 12, 2010

@author: pfl
'''
import unittest
import webimport.loadWebPage.loadWeb as loadWeb


class Test(unittest.TestCase):


    def testPrintWebPage(self):
        ''' noget med noget '''
        myLoader = loadWeb.loadWebClass()
        myLoader._printWebPage()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()