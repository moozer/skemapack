# -*- coding: UTF-8 -*-
'''
Testing basic tf import
@author: mon
'''
import unittest, os
from Input.TfImporter.TfCsvImport import TfCsvImport
from Datatypes.CourseData import CourseData

# Test data
TfInputCsvFile = "testdata/TF_skema.csv"
TfInputCsvDefaultMetaData = {'Weeknumbers by column': {}, 'Csv cell delimiter': '\t'}
TfInputCsvWeekNoByColumns = {1: 38, 2: 39, 3: 40, 4: 41, 5: 42, 6: 43, 27: 12, 28: 13, 29: 14, 30: 15, 31: 16, 32: 17, 33: 18, 34: 19, 35: 20, 36: 21, 37: 22, 38: 23, 39: 24, 40: 25, 41: 26, 42: 27, 43: 28, 44: 29, 45: 30, 46: 31, 47: 32, 48: 33, 49: 34, 50: 35, 51: 36, 52: 37}
TfInputCsvMetaData = dict( TfInputCsvDefaultMetaData.items()
                           + {'Weeknumbers by column': TfInputCsvWeekNoByColumns}.items()  )

Teacher1Initials = 'Teacher 7'
Teacher1Classes = [ CourseData( LessonsList = {40: 6, 41: 8, 43: 10, 39: 4}, 
                    Course = 'Subject H1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                    CourseData( LessonsList = {1: 4, 2: 4, 3: 4, 44: 4, 45: 4, 46: 4, 47: 4, 48: 4, 49: 4, 50: 4},
                    Course = 'Subject L1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                    CourseData( LessonsList = {1: 8, 2: 8, 3: 8, 50: 4}, 
                    Course = 'Subject O1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                    CourseData( LessonsList = {40: 6, 41: 8, 39: 4}, 
                    Course = 'Subject D1', Teacher = 'Teacher 7', Class = '1. Sem B Netv\xc3\xa6rk'),
                    CourseData( LessonsList = {40: 8, 41: 8, 43: 8, 39: 4}, 
                    Course = 'Subject G1', Teacher = 'Teacher 7', Class = '1. Sem B Netv\xc3\xa6rk'),
                    CourseData( LessonsList = {36: 4, 37: 6, 38: 8, 39: 10}, 
                    Course = 'Subject H1', Teacher = 'Teacher 7', Class = '1. Sem B Netv\xc3\xa6rk'),
                    CourseData( LessonsList = {1: 8, 2: 8, 3: 8, 44: 6, 45: 6, 46: 6, 47: 6, 48: 8, 49: 8, 50: 8}, 
                    Course = 'Subject T1', Teacher = 'Teacher 7', Class = '1. Sem B Netv\xc3\xa6rk')
                    ]
Teacher1FirstClass = Teacher1Classes[0]
TfNumEntriesTeacher1 = 9
Teacher2Initials = 'Teacher2'
Teacher2FirstClass = CourseData( LessonsList = {36: 4, 37: 4, 38: 4, 39: 4, 40: 4, 41: 4, 43: 4}, 
                                 Course = 'Subject B1', Teacher = 'Teacher2', Class = '1. Sem A Elektronik' )

TeacherData = { 'Teacher2': {'FirstCourse': Teacher2FirstClass},
               'Teacher 7': {'FirstCourse': Teacher1FirstClass} }

Class1Name = "1. Sem B Netværk"
Class1FirstClass = CourseData ( Course = 'Subject A1', LessonsList = {35: 9}, 
                                Teacher = 'Teacher 9', Class = '1. Sem B Netv\xc3\xa6rk' )


def RepeatTest( ParamList ):
    def RepeatT( TestToRun ):
        def Inner( *args, **kwargs ):
            for param in ParamList:
                ret = TestToRun( *args, **param ) 
            return ret
        return Inner
    return RepeatT


class Test(unittest.TestCase):
    def setUp(self):
        ''' makes a copy of the test data to avoid overwriting something '''
        self._StartDir = os.getcwd()
        try: # if it fails, then we are in the correct directory.
            os.chdir("testpackage/Input/testTfImporter")
        except:
            pass
        pass
    
    def tearDown(self):
        os.chdir(self._StartDir )
        pass
   
    def testConstruction(self):
        ''' TfImporter : test construction of TfCsvImport '''
        tfi = TfCsvImport(TfInputCsvFile )
        self.assertEqual( tfi.GetCsvFilename(), TfInputCsvFile )

    def testBadCsvFileName(self):
        ''' TfImporter : test use of bad filename '''
        self.assertRaises( ValueError, TfCsvImport, 'ThisFileDoesNotExist.csv' )

    def testNoCsvFileName(self):
        ''' TfImporter : test use of bad filename (None) '''
        self.assertRaises( ValueError, TfCsvImport, None )

    def testEnableSearchByTeacher(self):
        ''' TfImporter : test selecting teacher based search '''
        print os.getcwd()
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)
        self.assertEqual( tfi.IsSearchEnabled(), True )

    def testGetNextEntry(self):
        ''' TfImporter : test the retrieval of the first entry (Teacher1) '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        self.assertEqual( tfi.next(), Teacher1FirstClass )

    def testGetNextEntryWithDiffTeacher(self):
        ''' TfImporter : test the retrieval of the first entry (teacher2)'''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher2Initials)        
        self.assertEqual( tfi.next(), Teacher2FirstClass )

    def testRestartSearch(self):
        ''' TfImporter : test restarting search with new teacher '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        self.assertEqual( tfi.next(), Teacher1FirstClass )
        tfi.EnableImportByTeacher(Teacher2Initials)        
        self.assertEqual( tfi.next(), Teacher2FirstClass )

    def testGetNextEntryMultipleTimes(self):
        ''' TfImporter : test the retrieval of the mulitple entries '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
            
        for i in range(0, len(Teacher1Classes )):
            self.assertEqual( tfi.next(), Teacher1Classes[i] )
            
    def testGetDefaultMetadata(self):
        ''' TfImporter : test we have some base metadata '''
        tfi = TfCsvImport(TfInputCsvFile )
        self.assertEqual(tfi.GetMetaData(), TfInputCsvDefaultMetaData)

    def testGetMetadataAfterFirstEntry(self):
        ''' TfImporter : test that the metadata gets populated during retrieval of entries '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        tfi.next()
        self.assertEqual(tfi.GetMetaData(), TfInputCsvMetaData)
        
    @RepeatTest( [ {'Teacher': 'Teacher 7'}, {'Teacher': 'Teacher2'}] )
    def testGetNextEntryRepeated(self, Teacher):
        ''' test the retrieval of the first entry (by list)'''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher ) 
        self.assertEqual( tfi.next(), TeacherData[Teacher]['FirstCourse'] )

    def testIterator(self):
        ''' TfImporter : test using tfimporter as iterator '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
            
        i = 0
        for entry in tfi: #@UnusedVariable
            i += 1
        
        self.assertEqual( i, TfNumEntriesTeacher1 )
        
    def testGetNextEntryIterator(self):
        ''' TfImporter : Check use of TfCsvImporter as iterator '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher('Teacher 7' )
        
        count = 0
        for entry in tfi.GetNextEntryIterator(): #@UnusedVariable
            count = count +1
        self.assertEqual( count, 9, 'Wrong number of classes returned')
        
    def testGetNextEntryWithClass(self):
        ''' TfImporter : test the retrieval of the first entry (Class 1)'''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByClass(Class1Name)        
        self.assertEqual( tfi.next(), Class1FirstClass )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()
