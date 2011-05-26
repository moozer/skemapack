'''
Created on May 6, 2011

@author: morten
'''

import unittest, os
from Datatypes.ActivityDb import ActivityDb
from Datatypes.ActivityData import ActivityData
from testpackage.Utilities.SupportStuff import *
from testpackage.Utilities.TestdataSupport.DbToHtml import *

AD1 = ActivityData( Teacher = 'MON', Class = '2. semester network', Course = 'CourseA', 
                    LessonsList = {10: 1, 11: 2, 12: 3, 13: 4} )
AD2 = ActivityData( Teacher = 'MON', Class = '3. semester network', Course = 'CourseB', 
                    LessonsList = {10: 1, 11: 2, 12: 3, 13: 4} )
AD3 = ActivityData( Teacher = 'PFL', Class = '2. semester network', Course = 'CourseC', 
                    LessonsList = {10: 1, 11: 2, 12: 3, 13: 4} )
AD4 = ActivityData( Teacher = 'PFL', Class = '4. semester network', Course = 'CourseD', 
                    LessonsList = {10: 1, 11: 2, 12: 3, 13: 4} )



Teachers = { 'MON': 'Morten', 'PFL': 'Poul'}
TeacherIni = 'MON'
TeacherId = 1

AD_aux = ActivityData( Teacher = 'MON', Class = 'ClassName', Course = 'CourseName', 
                    LessonsList = {10: 1, 11: 2, 12: 3, 13: 4} )


class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        self._db = ActivityDb( ':memory:') 

        os.chdir(TempDataDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testConstructor(self):
        self.assertTrue( len( self._db.GetMetadata() ) > 0 )
        
    def testGetTeacherList(self):
        TeacherListFromDb = self._db.GetTeacherList()
        self.assertTrue( len( TeacherListFromDb ) > 0)

        for ini in Teachers.keys():
            self.assertEqual( TeacherListFromDb[ini], Teachers[ini])

    def testGetTeacherId(self):
        self.assertEqual( self._db.GetTeacherId( TeacherIni ), TeacherId )
        
    def testGetBadTeacherId(self):
        self.assertRaises( ValueError, self._db.GetTeacherId, "NonExistantTeacherInitials" )
        
    def testInsertActivityBadTeacherIni(self):
        AD_aux.setTeacher( "BadTeacherName ")
        self.assertRaises( ValueError, self._db.AddActivity, AD_aux )
        AD_aux.setTeacher( AD1.getTeacher())
        
        
    def testInsertAndRetrieve(self):
        self._db.AddActivity( AD1 )

        count = 0
        for ADFromDb in self._db.GetActivities():
            self.assertEqual( ADFromDb, AD1 )           # this test will pass if no activities are found !
            count += 1
        self.assertEqual( 1, count)
            
    def testInsertAndRetrieveEmptyLists(self):
        self._db.AddActivity( AD1 )
        count = 0
        for ADFromDb in self._db.GetActivities(Teachers=[]):
            self.assertEqual( ADFromDb, AD1 )
            count += 1
        self.assertEqual( 1, count)
       
    def testInsertAndRetrieveByTeacher(self):
        self._db.AddActivity( AD1 )
        self._db.AddActivity( AD2 )
        self._db.AddActivity( AD3 )
        self._db.AddActivity( AD4 )
        
        listOfAD = []
        for ADFromDb in self._db.GetActivities(Teachers=["PFL"]):
            listOfAD.append(ADFromDb)
        self.assertEqual( listOfAD, [AD3,AD4] )
       
    def testInsertAndRetrieveByClass(self):
        self._db.AddActivity( AD1 )
        self._db.AddActivity( AD2 )
        self._db.AddActivity( AD3 )
        self._db.AddActivity( AD4 )

        listOfAD = []
        for ADFromDb in self._db.GetActivities( Classes=["2. semester network"] ):
            listOfAD.append(ADFromDb)
        self.assertEqual( listOfAD, [AD1,AD3] )
       
    def testConstructorUsingExistingDb(self):
        try:
            self._db = ActivityDb( TestDbFilename )
        except:
            self.assertEqual( 1,0, "Failed to instantiate using db filename %s" % TestDbFilename)
                 
    def testFailOnNotExist(self):
        self.assertRaises( IOError, ActivityDb, ':memory:', u'NonExistIniFile', True)
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
