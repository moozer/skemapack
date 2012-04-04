'''
Created on Mar 29, 2012

@author: flindt
'''
import unittest

from Input.DumpCsv import DumpCsvFromXml
from Input import DumpCsv
import filecmp
from Configuration import SkemaPackConfig
import os,shutil

from Import.ImportFile import ImportFile
from Export.ExportHtml import ExportHtml

from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig

ExportHtmlWorkDir = "DumpCsv"
 

class Test(unittest.TestCase):

    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( ExportHtmlWorkDir )
        
        #self.myConfig = SkemaPackConfig( open( ExportHtmlCfgFile  ) )
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        #RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testLaunchCalc(self):
        model, desktop = DumpCsvFromXml.LaunchCalcWithFile( "test123.xls")
        model.dispose()
        DumpCsvFromXml.ShutdownCalc( desktop )
        pass

    def testNoInput(self):
        XmlFileName = "TF_skema.ods"
        CsvFileName = "TF_skema_test.csv"
        SheetName = "IT-Skema"
        Seperator = "\t"
        DumpCsvFromXml.DumpNamedSheet( XmlFileName, CsvFileName, SheetName, Seperator)
        
        #shutil.copy("TF_skema.csv", "TF_skema_test.csv")
        self.assertEqual( filecmp.cmp("TF_skema.csv", "TF_skema_test.csv", False), True)
        
        pass





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()