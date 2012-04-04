'''
Created on 4 Apr 2012

@author: moz
'''
import unittest
from Datatypes.ActivityData import ActivityData
from Datatypes.EventFunctions import AdToWeeksum

Ad = ActivityData( 'Teacher1', 'Class1', 'Course1', { 35: 9 } )
EventResult = [{'Class': 'Class1',
   'LessonCount': 9,
   'Subject': 'Course1',
   'Teacher': 'Teacher1',
   'Week': 35,
   'Year': 2012}]

class Test(unittest.TestCase):


    def testAdToEvent(self):
        event = AdToWeeksum( Ad )
        self.assertEqual(event, EventResult )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAdToEvent']
    unittest.main()