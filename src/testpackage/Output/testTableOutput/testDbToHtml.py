'''
Created on May 8, 2011

@author: morten
'''
import unittest, os
from testpackage.Utilities.SupportStuff import *

from Datatypes.ActivityDb import ActivityDb
from testpackage.Utilities.TestdataSupport.DbToHtml import *
from Output.TableOutput.TableOutput import TableOutput

TmpTableOutputFile = "temptable.html"

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


    def testDbToHtml(self):
        ADb = ActivityDb( TestDbFilename )
        
        
        TO = TableOutput( ADb.GetActivities(),
                          IncludeHeader=False, IncludeRowSums=False, 
                          IncludeColumnSums=False, IncludePreperation=False )
        HTML = TO.GetHtmlTable( RawHtmlWeekStart, RawHtmlWeekEnd )
        f = open(TmpTableOutputFile, 'w' )
        f.write( HTML )
        f.close()
        
        ret= os.system( 'diff %s %s  > /dev/null' % (RawHtmlTableOutput, TmpTableOutputFile ))
        self.assertEqual( ret, 0, "output table mismatch" )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()