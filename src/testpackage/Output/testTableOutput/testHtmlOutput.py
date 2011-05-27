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
        self.assertEqual( ObjectAsHtml, HO.GetHtmlTable() )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
