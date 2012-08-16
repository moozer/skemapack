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

ExportCsvWorkDir = "CsvOutput"
ExportCsvCfgFile = 'ExportCsv.cfg'
ExportCsvOutputfile = 'ExportCsvResult.csv'
ExportCsvKnownResult = 'ExportCsvKnownResult.csv'

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
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()