'''
Created on May 27, 2011

@author: morten
'''
import unittest

from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Output.TableOutput.HtmlOutput import HtmlOutput
from testpackage.Utilities.TestdataSupport.TableOutput import * #@UnusedWildImport


class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        #RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testSimpleHtmlOutput(self):
        HO = HtmlOutput( IterableObject )
        self.assertEqual( ObjectAsHtml, HO.GetHtmlTable(StartWeek=38, EndWeek=52) )
        pass

    def testHtmlCompare(self):
        HO = HtmlOutput( IterableObject, CmpObj = IterableObject )
        self.assertEqual( HtmlWithCompare_43_44, HO.GetHtmlTable(StartWeek=43, EndWeek=44) )
        pass
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
