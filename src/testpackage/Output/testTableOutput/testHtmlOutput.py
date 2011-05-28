'''
Created on May 27, 2011

@author: morten
'''
import unittest

from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Output.TableOutput.HtmlOutput import HtmlOutput
from testpackage.Utilities.TestdataSupport.TableOutput import * #@UnusedWildImport
from testpackage.Utilities.TestdataSupport.ActivityData import * 

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

    def testHtmlCompareEquals(self):
        HO = HtmlOutput( IterableObject, CmpObj = IterableObject )
        self.assertEqual( HtmlWithCompare_43_44, HO.GetHtmlTable(StartWeek=43, EndWeek=44) )
        pass
        
    def testHtmlCompareWithDiffs(self):
        HO = HtmlOutput( AD_DataSet1, CmpObj = AD_DataSet2)
        Html = HO.GetHtmlTable(StartWeek=43, EndWeek=44)
        self.assertEqual( HtmlWithCompareDiff_43_44, Html )
        pass
    
    def testHtmlCompareWithDiffLengths(self):
        HO = HtmlOutput( AD_DataSet1, CmpObj = AD_DataSet3)
        Html = HO.GetHtmlTable(StartWeek=Week1, EndWeek=WeekLast)
        self.assertEqual( HtmlWithCompareDiffLength, Html )
        pass
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
