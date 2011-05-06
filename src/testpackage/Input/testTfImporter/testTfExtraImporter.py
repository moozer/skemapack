'''
Created on Mar 3, 2011

@author: morten
'''
import unittest, os
from Input.TfImporter.TfExtraCsvImport import TfExtraCsvImport
from Datatypes.ActivityData import ActivityData

Teacher1Initials = 'Teacher 7'
TfExtraInputCsvFile = 'testdata/TF_extra_1.csv'
#Teacher1FirstEntry = {'Course': 'Vacation', 'Lessons by week': {3: 4, 5: 35, 6: 35, 7: 35}, 'Teacher': 'Teacher 7', 'Class': 'Teacher 7'}
Teacher1FirstEntry = ActivityData(Course = 'Vacation', LessonsList = {3: 4, 5: 35, 6: 35, 7: 35}, 
                                Teacher = 'Teacher 7', Class = 'Teacher 7' )
TfNumEntriesTeacher1 = 1

#set 2. one week only and decimal values
TfExtraInputCsvFile2 = 'testdata/TF_extra_2.csv'
TfExtraInputCsvFile2Entries = [
   ActivityData(Course = 'Vacation', LessonsList = {13: 4.0}, Teacher = 'Teacher 7', Class ='Teacher 7'),
   ActivityData(Course = 'Something else', LessonsList = {13: 1.5}, Teacher = 'Teacher 7', Class = 'Teacher 7')
]

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
        pass
    
    def tearDown(self):
        os.chdir(self._StartDir )
        pass
   
    def testConstruction(self):
        ''' TfExtraCvsImporter : test construction of TfCsvImport '''
        tfi = TfExtraCsvImport(TfExtraInputCsvFile )
        self.assertEqual( tfi.GetCsvFilename(), TfExtraInputCsvFile )

    def testBadCsvFileName(self):
        ''' TfExtraCvsImporter : test use of bad filename '''
        self.assertRaises( ValueError, TfExtraCsvImport, 'ThisFileDoesNotExist.csv' )

    def testNoCsvFileName(self):
        ''' TfExtraCvsImporter : test use of bad filename (None) '''
        self.assertRaises( ValueError, TfExtraCsvImport, None )

    def testEnableSearchByTeacher(self):
        ''' TfExtraCvsImporter : test selecting teacher based search '''
        print os.getcwd()
        tfi = TfExtraCsvImport(TfExtraInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)
        self.assertEqual( tfi.IsSearchEnabled(), True )

    def testGetNextEntry(self):
        ''' TfExtraCvsImporter : test the retrieval of the first entry (Teacher1) '''
        tfi = TfExtraCsvImport(TfExtraInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        self.assertEqual( tfi.next(), Teacher1FirstEntry )
        
    def testIterator(self):
        ''' TfExtraCvsImporter : test using tfimporter as iterator '''
        tfi = TfExtraCsvImport(TfExtraInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
            
        i = 0
        for entry in tfi: #@UnusedVariable
            i += 1
        
        self.assertEqual( i, TfNumEntriesTeacher1 )
       
    def testDecimalAsWeekValue(self):
        ''' TfExtraCvsImporter : test retrieve decimal hours.'''
        tfi = TfExtraCsvImport(TfExtraInputCsvFile2 )
        tfi.EnableImportByTeacher(Teacher1Initials)        
            
        i = 0
        for entry in tfi: #@UnusedVariable
            self.assertEqual( TfExtraInputCsvFile2Entries[i], entry )
            i += 1
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()