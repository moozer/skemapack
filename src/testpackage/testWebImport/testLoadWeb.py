'''
Created on Oct 12, 2010

@author: pfl
'''
import unittest
import webimport.loadWebPage.loadWeb as loadWeb


class Test(unittest.TestCase):


    def testPrintWebPage(self):
        myLoader = loadWeb.loadWebClass()
        myLoader.printWebPage()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()