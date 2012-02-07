'''
Created on 7 Feb 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
from Export.ExportFile import ExportFile
from Convert.ConvertToWeeksum import ConvertToWeeksum

ImportFileWorkDir = 'ImportFile'
ImportFileCfgFilename = 'ImportFile.cfg'

# TODO: Sums are wrong due to bad 'date' in events.
ResultSum = [{'Week': 34, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 34, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 35, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 35, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011}]

class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( ImportFileWorkDir)
        
        self.myConfig = SkemaPackConfig( open( ImportFileCfgFilename ) )
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testSimpleConvert(self):
        ''' ConvertToWeeksum : basic init '''
        events = ImportFile( self.myConfig )
        Sum = ConvertToWeeksum( events, self.myConfig )
        self.assertEqual(Sum, ResultSum )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()