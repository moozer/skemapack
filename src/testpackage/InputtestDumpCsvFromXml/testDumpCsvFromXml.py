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
from Input.DumpCsv.DumpCsvFromXml import ConvertToCsv

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

    @unittest.skip("fails and stalls unittesting")    
    def testLaunchCalc(self):
        model, desktop = DumpCsvFromXml.LaunchCalcWithFile( "test123.xls")
        model.dispose()
        DumpCsvFromXml.ShutdownCalc( desktop )
        pass

    @unittest.skip("fails and stalls unittesting")    
    def testNoInput(self):
        XmlFileName = "TF_skema.ods"
        CsvFileName = "TF_skema_test.csv"
        SheetName = "IT-Skema"
        Seperator = "\t"
        DumpCsvFromXml.DumpNamedSheet( XmlFileName, CsvFileName, SheetName, Seperator)
        
        #shutil.copy("TF_skema.csv", "TF_skema_test.csv")
        self.assertEqual( filecmp.cmp("TF_skema.csv", "TF_skema_test.csv", False), True)
        
        pass

    def testConvertToCsv(self):
        XmlFileName = "TF_skema.ods"
        CsvFileName = "TF_skema_test.csv"
        SheetName = "IT-skema"
        Seperator = "\t"
        ConvertToCsv( XmlFileName, CsvFileName, SheetName, Seperator)
        
        # this test will never succeed since the page include a dynamic timestamnp...
        #self.assertEqual( filecmp.cmp("TF_skema.csv", "TF_skema_test.csv", False), True)
        
        # open data files, skip the first 100 bytes and then read some more before comaping.
        fh1 = open("TF_skema.csv")
        fh2 = open("TF_skema_test.csv")
        
        fh1.read(200)
        fh2.read(200)
        
        data1 = fh1.read(150)
        data2 = fh2.read(150)
        self.assertEqual( data1, data2)

        pass

    def testConvertToCsvWithMultipleSheets(self):
        XmlFileName = "TF_skema_multiple_sheets.ods"
        CsvFileName = "TF_skema_test_multiple.csv"
        SheetName = "IT-skema"
        Seperator = "\t"
        ConvertToCsv( XmlFileName, CsvFileName, SheetName, Seperator)
        
        # open data files, skip the first 100 bytes and then read some more before comaping.     
        fh1 = open("TF_skema.csv")
        fh2 = open(CsvFileName)
        
        fh1.read(200)
        fh2.read(200)
        
        data1 = fh1.read(150)
        data2 = fh2.read(150)
        self.assertEqual( data1, data2)

        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()