'''
Created on Aug 12, 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import CloneTestData, ChDirToSrc,\
    TempDataDir, RemoveTestData
import os
from Output.CsvOutput import CsvOutput

WorkDir = 'CsvOutput'
Weeksums = [{'Week': 32, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 32, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 33, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 33, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}]

Weeksums2Years = [{'Week': 2, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2013, 'Teacher': 'mon'}, 
             {'Week': 2, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2013, 'Teacher': 'mon'}, 
             {'Week': 51, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2012, 'Teacher': 'mon'}, 
             {'Week': 51, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2012, 'Teacher': 'mon'}]


ResultCsv = [
    [u'Class', u'Subject', u'2011-32', u'2011-33'],
    [u'11OIT3bH2', u'Adv. networking', 4, 2 ],
    [u'11OIT3bH2', u'IT Security', 5, 3 ]
]



class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( WorkDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testBasicTableoutput(self):
        ''' HtmlTableOutput : basic output '''
        CsvList = CsvOutput( Weeksums )
        self.assertEqual( ResultCsv, CsvList )
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()