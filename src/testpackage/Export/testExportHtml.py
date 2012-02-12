'''
Created on 10 Feb 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig

from Export.ExportHtml import ExportHtml
import filecmp

ExportHtmlWorkDir = "ExportHtml"
ExportHtmlCfgFile = "ExportHtml.cfg"
ExportHtmlKnownResult = "KnownExportHtml.html"
ExportHtmlOutputfile = "ExportHtml.html"


WeeksumData = [{'Week': 34, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 34, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 35, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 35, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011}]


class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( ExportHtmlWorkDir )
        
        self.myConfig = SkemaPackConfig( open( ExportHtmlCfgFile  ) )
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testBasicTable(self):
        ExportHtml( WeeksumData, self.myConfig) 
        self.assertTrue( filecmp.cmp(ExportHtmlOutputfile, ExportHtmlKnownResult) )
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()