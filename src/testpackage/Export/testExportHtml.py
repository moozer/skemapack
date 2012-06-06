'''
Created on 10 Feb 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
from Export.ExportHtml import ExportHtml
import filecmp

ExportHtmlWorkDir = "ExportHtml"
ExportHtmlCfgFile = "ExportHtml.cfg"
ExportHtmlKnownResult = "KnownExportHtml.html"
ExportHtmlWithSumsKnownResult = "KnownExportHtmlWithSums.html"
ExportHtmlOutputfile = "ExportHtml.html"

WeeksumData = [{'Week': 34, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 34, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}]

WeeksumDataUnsorted = [
             {'Week': 34, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
            {'Week': 34, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 35, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}
             ]


ExportHtmlSemesterOutput = "ExportHtmlSemester.html"
ExportHtmlSemesterKnownResult = "KnownExportHtmlSemester.html"
ExportHtmlWithTeacherKnownResult = "KnownExportHtmlWithTeacher.html"

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
    
    #@unittest.skip("reenable me")
    def testCompleteSemesterFail(self):
        ''' ExportHtml : recreate error running exporthtml on real semester dataset '''
        ws, config = ImportFile( self.myConfig, "ImportFileSemester" ) #@UnusedVariable
        ExportHtml( ws, self.myConfig, "ExportHtmlSemester") 
        self.assertTrue( filecmp.cmp(ExportHtmlSemesterOutput, ExportHtmlSemesterKnownResult) )
        
    #@unittest.skip("reenable me")
    def testTableWithBothSums(self):
        ''' ExportHtml : Export to html with both row and column sums '''
        ExportHtml( WeeksumData, self.myConfig, ConfigSet = 'ExportHtmlWithSums' ) 
        self.assertTrue( filecmp.cmp(ExportHtmlOutputfile, ExportHtmlWithSumsKnownResult) )
        pass
        
    def testTableExportWithUnsortedData(self):
        ''' ExportHtml : Export to html of unsorted data '''
        ExportHtml( WeeksumDataUnsorted, self.myConfig, ConfigSet = 'ExportHtmlWithSums' ) 
        self.assertTrue( filecmp.cmp(ExportHtmlOutputfile, ExportHtmlWithSumsKnownResult) )
        pass
        
    def testTableExportWithTeacher(self):
        ''' ExportHtml : Export to html with teacher included '''
        ExportHtml( WeeksumDataUnsorted, self.myConfig, ConfigSet = 'ExportHtmlWithTeacher' ) 
        self.assertTrue( filecmp.cmp(ExportHtmlOutputfile, ExportHtmlWithTeacherKnownResult) )
        pass
        
    def testExportOfNoData(self):
        ExportHtml( [], self.myConfig, ConfigSet = 'ExportHtmlWithTeacher' ) 
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()