#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on May 20, 2011

@author: flindt
'''
import unittest
import time
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Datatypes.ActivityData import ActivityData
from Datatypes.ActivityPlan import ActivityPlan


Teacher1 = 'TeacherIni'
Teacher1Name = 'Teachers 1 Real Name'
Class1 = 'ClassName'
Course1 = 'CourseName'
LessonsByWeek1 = {10: 1, 11: 2, 12: 3, 13: 4}
WeekList1 = [10, 11, 12, 13]
Week1 = 10
LessonsInWeek1= 1

AD1 = ActivityData( Teacher = Teacher1, Class = Class1, Course = Course1, LessonsList = LessonsByWeek1 )
AD1_2 = ActivityData( Teacher = Teacher1, Class = Class1, Course = Course1, LessonsList = LessonsByWeek1 )

Teacher2 = 'Teacher2Ini'
Teacher2Name = 'Teachers 2 Real Name'
Class2 = 'ClassName2'
Course2 = 'CourseName2'
LessonsByWeek2 = {20: 11, 21: 22, 22: 12, 23: 34}
AD2 = ActivityData( Teacher = Teacher2, Class = Class2, Course = Course2, LessonsList = LessonsByWeek2 )



ChDirToSrc()
AP = ActivityPlan( ActData=AD1, TeacherFullName=Teacher1Name, \
                           PlanRelPath="1. Semester Common", PlanFileName="CourseName", \
                           PlansRootFolder="testpackage/Datatypes/Testfiles/RootPlanFolder" \
                           )
AP_1 = ActivityPlan( ActData=AD1, TeacherFullName=Teacher1Name, \
                           PlanRelPath="1. Semester Common", PlanFileName="CourseName", \
                           PlansRootFolder="testpackage/Datatypes/Testfiles/RootPlanFolder" \
                           )
AP2 = ActivityPlan( ActData=AD2, TeacherFullName=Teacher2Name, \
                           PlanRelPath="1. Semester Common", PlanFileName="CourseName2", \
                           PlansRootFolder="testpackage/Datatypes/Testfiles/RootPlanFolder" \
                           )


class Test(unittest.TestCase):


    def testConstructor(self):
        self.assertEquals(AP.getActData(), AD1)
        self.assertNotEquals(AP.getActData(), AD2)
        self.assertEquals(AP.getTeacherFullName(), 'Teachers 1 Real Name')
        self.assertEquals(AP.getPlanRelPath(), "1. Semester Common")
        self.assertEquals(AP.getPlanFileName(), "CourseName")
        self.assertEquals(AP.getPlansRootFolder(), "testpackage/Datatypes/Testfiles/RootPlanFolder")
        pass
    
    def testEqual(self):
        self.assertTrue( AP == AP_1 )
        
    def testNotEqual(self):
        self.assertTrue( AP != AP2 )
        
    def testGetLastUpdatedDate(self):
        ''' ActivityPlan : sanity check of current year '''
        # TODO: hard coded year?!
        self.assertTrue( AP.getLastUpdatedDate().tm_year ==2012 ) 
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConstructor']
    unittest.main()