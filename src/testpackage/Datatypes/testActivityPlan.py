#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on May 20, 2011

@author: flindt
'''
import unittest
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




class Test(unittest.TestCase):


    def testConstructor(self):
        self._StartDir = ChDirToSrc()
        AP = ActivityPlan( ActData=AD1, TeacherFullName=Teacher1Name, \
                           PlanRelPath="1. Semester", PlanFileName="CourseName", \
                           PlansRootFolder="testpackage/Datatypes/Testfiles/RootPlanFolder" \
                           )
        self.assertEquals(AP.getActData(), AD1)
        self.assertNotEquals(AP.getActData(), AD2)
        self.assertEquals(AP.getTeacherFullName(), 'Teachers 1 Real Name')
        self.assertEquals(AP.getPlanRelPath(), "1. Semester")
        self.assertEquals(AP.getPlanFileName(), "CourseName")
        self.assertEquals(AP.getPlansRootFolder(), "testpackage/Datatypes/Testfiles/RootPlanFolder")
        pass




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConstructor']
    unittest.main()