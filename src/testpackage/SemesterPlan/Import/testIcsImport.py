'''
Created on Sep 7, 2011

@author: morten
'''
import unittest

from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from SemesterPlan.Import.IcsImport import IcsImport
from datetime import date

BadIcsFilename = "ThisFileDoesNotExist"
IcsFile = "SemesterPlanImport/test.ics"
FirstEnry = {'StartDate': date(2012, 1, 11), 
             'EndDate': date(2012, 1, 13), 
             'Description': u'Questions, procedures and other details will be made available at a later date.', 
             'Summary': u'3rd semester oral exam (preliminary)'}

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


    @unittest.skip( "this part is currently unused")
    def testIcsImportBasicIteration(self):
        for entry in IcsImport( IcsFile ):
            self.assertEqual(True, True)
            print entry
        pass

    @unittest.skip( "this part is currently unused")
    def testIcsImportFirstEntry(self):
        for entry in IcsImport( IcsFile ):
            self.assertEqual(entry, FirstEnry)
            break
        
    @unittest.skip( "this part is currently unused")
    def testIcsImportBadFilename(self):
        try:
            for entry in IcsImport( BadIcsFilename ): #@UnusedVariable
                break
        except (IOError):
            pass
        except:
            self.assertTrue( False, "failed to get exception")
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()