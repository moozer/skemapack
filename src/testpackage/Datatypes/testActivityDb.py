'''
Created on May 6, 2011

@author: morten
'''

import unittest, os
from Datatypes.ActivityDb import ActivityDb
from Datatypes.ActivityData import ActivityData
from testpackage.Utilities.SupportStuff import *
from testpackage.Utilities.TestdataSupport.DbToHtml import *

AD1 = ActivityData( Teacher = 'MON', Class = '2. semester network', Course = 'CourseName', 
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

        for ADFromDb in self._db.GetActivities():
            self.assertEqual( ADFromDb, AD1 )
       
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