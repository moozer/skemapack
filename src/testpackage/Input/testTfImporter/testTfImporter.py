# -*- coding: UTF-8 -*-
'''
Testing basic tf import
@author: mon
'''
import unittest
from Input.TfImporter.TfCsvImport import TfCsvImport
from Datatypes.ActivityData import ActivityData
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport


# Test data
TfInputCsvFile = "TfImporter/TF_skema.csv"
TfInputCsvDefaultMetaData = {'Weeknumbers by column': {}, 'Csv cell delimiter': '\t'}
#TfInputCsvWeekNoByColumns = {'2012-02-06': 43, '2012-11-12': 31, '2012-11-19': 32, '2012-10-15': 27, '2012-12-17': 36, '2012-01-02': 38, '2012-12-10': 35, '2012-01-09': 39, '2012-09-03': 21, '2012-01-23': 41, '2012-07-30': 16, '2012-09-24': 24, '2012-07-16': 14, '2012-11-26': 33, '2012-08-13': 18, '2012-11-05': 30, '2012-10-08': 26, '2012-10-29': 29, '2012-10-01': 25, '2012-10-22': 28, '2012-01-16': 40, '2012-12-03': 34, '2012-09-17': 23, '2012-12-24': 37, '2012-07-23': 15, '2012-01-30': 42, '2012-09-10': 22, '2012-07-02': 12, '2012-08-06': 17, '2012-08-20': 19, '2012-08-27': 20, '2012-07-09': 13}
#TfInputCsvWeekNoByColumns = {1: 38, 2: 39, 3: 40, 4: 41, 5: 42, 6: 43, 27: 12, 28: 13, 29: 14, 30: 15, 31: 16, 32: 17, 33: 18, 34: 19, 35: 20, 36: 21, 37: 22, 38: 23, 39: 24, 40: 25, 41: 26, 42: 27, 43: 28, 44: 29, 45: 30, 46: 31, 47: 32, 48: 33, 49: 34, 50: 35, 51: 36, 52: 37}
TfInputCsvWeekNoByColumns = {'2012-32': 17, '2012-33': 18, '2012-30': 15, '2012-31': 16, '2012-36': 21, 
                             '2012-37': 22, '2012-34': 19, '2012-35': 20, '2012-38': 23, '2012-39': 24, 
                             '2012-50': 35, '2012-51': 36, '2012-52': 37, '2013-2': 39, '2013-3': 40, 
                             '2013-1': 38, '2013-6': 43, '2013-4': 41, '2013-5': 42, '2012-27': 12, 
                             '2012-29': 14, '2012-28': 13, '2012-47': 32, '2012-46': 31, '2012-45': 30, 
                             '2012-44': 29, '2012-43': 28, '2012-42': 27, '2012-41': 26, '2012-40': 25, 
                             '2012-49': 34, '2012-48': 33}
TfInputCsvMetaData = dict( TfInputCsvDefaultMetaData.items()
                           + {'Weeknumbers by column': TfInputCsvWeekNoByColumns}.items()  )

Teacher1Initials = 'Teacher 7'
#Teacher1Classes = [ ActivityData( LessonsList = {'2012-09-24': 4, '2012-10-01': 6, '2012-10-08': 8, '2012-10-22': 10}, 
#                    Course = 'Subject H1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
#                    ActivityData( LessonsList = {1: 4, 2: 4, 3: 4, 44: 4, 45: 4, 46: 4, 47: 4, 48: 4, 49: 4, 50: 4},
#                    Course = 'Subject L1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
#                    ActivityData( LessonsList = {1: 8, 2: 8, 3: 8, 50: 4}, 
#                    Course = 'Subject O1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
#                    ActivityData( LessonsList = {40: 6, 41: 8, 39: 4}, 
#                    Course = 'Subject D1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk'),
#                    ActivityData( LessonsList = {40: 8, 41: 8, 43: 8, 39: 4}, 
#                    Course = 'Subject G1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk'),
#                    ActivityData( LessonsList = {36: 4, 37: 6, 38: 8, 39: 10}, 
#                    Course = 'Subject H1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk'),
#                    ActivityData( LessonsList = {1: 8, 2: 8, 3: 8, 44: 6, 45: 6, 46: 6, 47: 6, 48: 8, 49: 8, 50: 8}, 
#                    Course = 'Subject T1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk')
#                    ]
Teacher1Classes = [ ActivityData( LessonsList = {'2012-39': 4, '2012-43': 10, '2012-41': 8, '2012-40': 6}, 
                    Course = 'Subject H1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                    ActivityData( LessonsList = {'2013-1': 4, '2013-2': 4, '2013-3': 4, 
                                                 '2012-44': 4, '2012-45': 4, '2012-46': 4, 
                                                 '2012-47': 4, '2012-48': 4, '2012-49': 4, 
                                                 '2012-50': 4},
                    Course = 'Subject L1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                    ActivityData( LessonsList = {'2013-1': 8, '2013-2': 8, '2013-3': 8, 
                                                 '2012-50': 4}, 
                    Course = 'Subject O1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                    ActivityData( LessonsList = {'2012-40': 6, '2012-41': 8, '2012-39': 4}, 
                    Course = 'Subject D1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk'),
                    ActivityData( LessonsList = {'2012-40': 8, '2012-41': 8, '2012-43': 8, 
                                                 '2012-39': 4}, 
                    Course = 'Subject G1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk'),
                    ActivityData( LessonsList = {'2012-36': 4, '2012-37': 6, '2012-38': 8, 
                                                 '2012-39': 10}, 
                    Course = 'Subject H1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk'),
                    ActivityData( LessonsList = {'2013-1': 8, '2013-2': 8, '2013-3': 8, 
                                                 '2012-44': 6, '2012-45': 6, '2012-46': 6, 
                                                 '2012-47': 6, '2012-48': 8, '2012-49': 8, 
                                                 '2012-50': 8}, 
                    Course = 'Subject T1', Teacher = 'Teacher 7', Class = '1. Sem B Netværk')
                    ]
Teacher1FirstClass = Teacher1Classes[0]
TfNumEntriesTeacher1 = 9
Teacher2Initials = 'Teacher2'
Teacher2FirstClass = ActivityData( LessonsList = {"2012-36": 4, "2012-37": 4, "2012-38": 4, 
                                                  "2012-39": 4, "2012-40": 4, "2012-41": 4, 
                                                  "2012-43": 4}, 
                                 Course = 'Subject B1', Teacher = 'Teacher2', Class = '1. Sem A Elektronik' )

TeacherData = { 'Teacher2': {'FirstCourse': Teacher2FirstClass},
               'Teacher 7': {'FirstCourse': Teacher1FirstClass} }

Class1Name = "1. Sem B Netværk"
Class1FirstClass = ActivityData ( Course = 'Subject A1', LessonsList = {"1999-35": 9}, 
                                Teacher = 'Teacher 9', Class = '1. Sem B Netværk' )

FirstActivityInFile = ActivityData( "Teacher1", "1. Sem A Elektronik", "Subject A1", {"1999-35": 9})

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
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass
   
    def testConstruction(self):
        ''' TfImporter : test construction of TfCsvImport '''
        tfi = TfCsvImport(TfInputCsvFile , StartYear="2012" )
        self.assertEqual( tfi.GetCsvFilename(), TfInputCsvFile )

    def testBadCsvFileName(self):
        ''' TfImporter : test use of bad filename '''
        self.assertRaises( ValueError, TfCsvImport, 'ThisFileDoesNotExist.csv' )

    def testNoCsvFileName(self):
        ''' TfImporter : test use of bad filename (None) '''
        self.assertRaises( ValueError, TfCsvImport, None )

    def testEnableSearchByTeacher(self):
        ''' TfImporter : test selecting teacher based search '''
        tfi = TfCsvImport(TfInputCsvFile, StartYear="2012"  )
        tfi.EnableImportByTeacher(Teacher1Initials)
        self.assertEqual( tfi.IsSearchEnabled(), True )

    def testGetNextEntry(self):
        ''' TfImporter : test the retrieval of the first entry (Teacher1) '''
        tfi = TfCsvImport(TfInputCsvFile , StartYear="2012" )
        tfi.EnableImportByTeacher(Teacher1Initials)  
        #print(tfi.next())      
        ad = tfi.next()
        self.assertEqual( ad, Teacher1FirstClass )

    def testGetNextEntryWithDiffTeacher(self):
        ''' TfImporter : test the retrieval of the first entry (teacher2)'''
        tfi = TfCsvImport(TfInputCsvFile, StartYear="2012"  )
        tfi.EnableImportByTeacher(Teacher2Initials)        
        self.assertEqual( tfi.next(), Teacher2FirstClass )

    def testRestartSearch(self):
        ''' TfImporter : test restarting search with new teacher '''
        tfi = TfCsvImport(TfInputCsvFile , StartYear="2012" )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        self.assertEqual( tfi.next(), Teacher1FirstClass )
        tfi.EnableImportByTeacher(Teacher2Initials)
        ad = tfi.next()
        self.assertEqual( ad, Teacher2FirstClass )

    def testGetNextEntryMultipleTimes(self):
        ''' TfImporter : test the retrieval of the mulitple entries '''
        tfi = TfCsvImport(TfInputCsvFile, StartYear="2012"  )
        tfi.EnableImportByTeacher(Teacher1Initials)        
            
        for i in range(0, len(Teacher1Classes )):
            ad = tfi.next()
            self.assertEqual( ad, Teacher1Classes[i], "entry #%d mismatch"%i )
            
    def testGetDefaultMetadata(self):
        ''' TfImporter : test we have some base metadata '''
        tfi = TfCsvImport(TfInputCsvFile , StartYear="2012" )
        self.assertEqual(tfi.GetMetaData(), TfInputCsvDefaultMetaData)

    def testGetMetadataAfterFirstEntry(self):
        ''' TfImporter : test that the metadata gets populated during retrieval of entries '''
        tfi = TfCsvImport(TfInputCsvFile, StartYear="2012" )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        tfi.next()
        MD = tfi.GetMetaData()
        self.assertEqual(tfi.GetMetaData(), TfInputCsvMetaData)
        
    @RepeatTest( [ {'Teacher': 'Teacher 7'}, {'Teacher': 'Teacher2'}] )
    def testGetNextEntryRepeated(self, Teacher):
        ''' test the retrieval of the first entry (by list)'''
        tfi = TfCsvImport(TfInputCsvFile, StartYear="2012"  )
        tfi.EnableImportByTeacher(Teacher ) 
        self.assertEqual( tfi.next(), TeacherData[Teacher]['FirstCourse'] )

    def testIterator(self):
        ''' TfImporter : test using tfimporter as iterator '''
        tfi = TfCsvImport(TfInputCsvFile , StartYear="2012" )
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
        ad = tfi.next()
        self.assertEqual( ad, Class1FirstClass )

    def testGetNextEntryEverything(self):
        ''' TfImporter : test the retrieval of the first entry (Class 1)'''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportAll()        
        ADFromDb = tfi.next()
        self.assertEqual( ADFromDb, FirstActivityInFile )

        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()
