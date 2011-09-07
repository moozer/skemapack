'''
Created on Sep 7, 2011

@author: morten
'''
import unittest

from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from SemesterPlan.Import.IcsImport import IcsImport

IcsFile = "SemesterPlanImport/test.ics"
BadIcsFilename = "ThisFileDoesNotExist"

class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass


    def testIcsImportBasicIteration(self):
        for entry in IcsImport( IcsFile ):
            self.assertEqual(True, True)
        pass

    def testIcsImportFirstEntry(self):
        for entry in IcsImport( IcsFile ):
            self.assertEqual(entry, "something")
            break
        
    def testIcsImportBadFilename(self):
        try:
            for entry in IcsImport( BadIcsFilename ):
                break
        except (IOError):
            pass
        except:
            self.assertTrue( False, "failed to get exception")
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()