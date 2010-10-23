'''
Created on Oct 12, 2010

@author: pfl
'''
import unittest
import Input.HtmlGetter.loadWebPage.loadHtml as loadWeb

class Test(unittest.TestCase):


    def testPrintWebPage(self):
        ''' helper function for development '''
        myLoader = loadWeb.htmlGetter()
        myLoader._printWebPage()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()