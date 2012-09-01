# -*- coding: UTF-8 -*-
'''
Created on Aug 12, 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import CloneTestData, ChDirToSrc,\
    RemoveTestData, TempDataDir
from Configuration.SkemaPackConfig import SkemaPackConfig
import os
import filecmp
from Export.ExportCsv import ExportCsv

WeeksumData = [{'Week': 34, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 34, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}]

WeeksumDataWithSpecChars = [
             {'Week': 34, 'LessonCount': 5, 'Subject': u'IT Security åæø', 'Class': u'11OIT3bH2å', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 34, 'LessonCount': 4, 'Subject': u'Adv. networking', 'Class': u'11OIT3bH2å', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 3, 'Subject': u'IT Security øæå', 'Class': u'11OIT3bH2å', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 2, 'Subject': u'Adv. networking', 'Class': u'11OIT3bH2å', 'Year': 2011, 'Teacher': 'mon'}]

ExportCsvWorkDir = "CsvOutput"
ExportCsvCfgFile = 'ExportCsv.cfg'
ExportCsvOutputfile = 'ExportCsvResult.csv'
ExportCsvKnownResult = 'ExportCsvKnownResult.csv'
ExportCsvWithSpecCharsKnownResult = 'ExportCsvWithSpecCharsKnownResult.csv'

class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( ExportCsvWorkDir )
        
        self.myConfig = SkemaPackConfig( open( ExportCsvCfgFile  ) )
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testBasicTable(self):
        ExportCsv( WeeksumData, self.myConfig) 
        self.assertTrue( filecmp.cmp(ExportCsvOutputfile, ExportCsvKnownResult) )
        pass
    
    def testOutputWithSpecialChars(self):
        ExportCsv( WeeksumDataWithSpecChars, self.myConfig) 
        self.assertTrue( filecmp.cmp(ExportCsvOutputfile, ExportCsvWithSpecCharsKnownResult) )
        pass
 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()