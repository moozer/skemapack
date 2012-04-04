'''
Created on Mar 29, 2012

@author: flindt
'''
import unittest

from Input.DumpCsv import DumpCsvFromXml
from Input import DumpCsv
import filecmp
from Configuration import SkemaPackConfig
import os

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
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testNoInput(self):
        XmlFileName = None 
        CsvFileName = None
        SheetName = None
        Seperator = None
        DumpCsvFromXml.DumpNamedSheet( XmlFileName, CsvFileName, SheetName, Seperator)
        
        
        pass





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()