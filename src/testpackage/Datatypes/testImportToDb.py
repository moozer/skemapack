'''
Created on May 7, 2011

@author: morten
'''
import unittest, os
from Input.TfImporter.TfCsvImport import TfCsvImport
from Datatypes.ActivityDb import ActivityDb

TfInputCsvFile = "testdata/TF_skema.csv"
TempDbFile = "testdata/testDb.sqlite"
TestBaseDbFile = "../../Utilities/testdata/TfToDb/BaseDb.sql"
NumActivitiesInCSV = 50

class Test(unittest.TestCase):
    def setUp(self):
        self._StartDir = os.getcwd()
        this_dir = os.path.dirname( __file__ )
        while 1 == 1:
            this_dir, tail = os.path.split( this_dir )
            if tail == 'src': # always go to src as default dir.
                this_dir = os.path.join( this_dir, tail )
                break
        os.chdir( this_dir )
        
        try: # if it fails, then we are in the correct directory.
            os.chdir("testpackage/Input/testTfImporter")
        except:
            pass

        if os.path.isfile(TempDbFile):
            os.remove(TempDbFile)
        pass
    
    def tearDown(self):
        if os.path.isfile(TempDbFile):
            os.remove(TempDbFile)
        
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