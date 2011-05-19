'''
Created on May 7, 2011

@author: morten
'''
import unittest, os
from Input.TfImporter.TfCsvImport import TfCsvImport
from Datatypes.ActivityDb import ActivityDb
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport

TfInputCsvFile = "TfImporter/TF_skema.csv"
TempDbFile = "testDb.sqlite"
TestBaseDbFile = "../../Utilities/testdata/TfToDb/BaseDb.sql"
NumActivitiesInCSV = 50

class Test(unittest.TestCase):
    ''' Testing HtmlToIcs from an external shell like perspective '''
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

    def testImportTfToDb(self):
        tfi = TfCsvImport( TfInputCsvFile )
        db = ActivityDb( TempDbFile,TestBaseDbFile )
        tfi.EnableImportAll()
    
        i = 0    
        for Activity in tfi:
            i = i+1
            db.AddActivity(Activity)
            
        self.assertEqual( i, NumActivitiesInCSV )



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()