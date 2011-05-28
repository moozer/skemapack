'''
Created on May 5, 2011

@author: morten
'''
import unittest
from Datatypes.ActivityData import ActivityData
from testpackage.Utilities.TestdataSupport.ActivityData import * 


TeacherTestNAme = "TestName"

class TestActivityData(unittest.TestCase):


    def testActivityDataConstructor(self):
        ''' TestActivityData.testCourseDataConstructor : basic contructor values '''
        CD = ActivityData( Teacher = Teacher1, Class = Class1, Course = Course1, LessonsList = LessonsByWeek1 )
        self.assertEqual( CD.getTeacher(), Teacher1 )
        self.assertEqual( CD.getClass(), Class1 )
        self.assertEqual( CD.getCourse(), Course1 )
        self.assertEqual( CD.getLessonsList(), LessonsByWeek1 )
        pass

    def testEqual(self):
        self.assertTrue( CD1 == CD1_2 )
        
    def testNotEqual(self):
        self.assertTrue( CD1 != CD2 )
        
    def testGetWeekNo(self):
        self.assertTrue( WeekList1 == CD1.getListOfWeeks() )

    def testGetWeekValue(self):
        self.assertTrue( CD1.getLessons(Week1) == LessonsInWeek1 )
        
    def testSetTeacher(self):
        CD_aux.setTeacher(TeacherTestNAme)
        self.assertEqual( TeacherTestNAme, CD_aux.getTeacher( ))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()