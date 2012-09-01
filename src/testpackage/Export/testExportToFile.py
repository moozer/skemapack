#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
from Export.ExportFile import ExportFile
from testpackage.Import.testImportFile import ImportFileData, ImportFileWorkDir, ImportFileCfgFilename
import sys
from testpackage.Utilities.TestdataSupport.WeeksumData import * 
import filecmp
import codecs
# using the same vars as testImportFile

ExportFileTestFileName = "teststdout.txt"
ExportFileWeeksumKnownResult = "WeeksumKnownResult.txt"
ExportfileResultFile = "ExportFileData.txt"

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

    def testBasicExportAndImport(self):
        ''' ExportFile : basic write+read test '''
        ExportFile(ImportFileData, self.myConfig )
        Events, config  = ImportFile(self.myConfig, 'ImportExportedFile') #@UnusedVariable
        self.assertEqual( Events, ImportFileData )
        pass
    
    def testConfigObjectNone(self):
        ''' ExportFile : test if ExportFile can handle None as config object '''
        old_stdout = sys.stdout
        fp = file( ExportFileTestFileName, 'w+' )
        sys.stdout = fp 
        ExportFile( ImportFileData ) # exprot using defaults
        sys.stdout = old_stdout
        fp.close()
        pass

    def testSaveWeeksums(self):
        ''' ExportFile : test if exportfile can handle weeksums '''
        ExportFile(ImportFileTestDataSum, self.myConfig )
        self.assertTrue( filecmp.cmp( ExportfileResultFile, ExportFileWeeksumKnownResult, shallow=False ) )
        pass
    
    def testReadWriteSpecialChars(self):
        ''' ExportFile : test if exportfile can handle æøå '''
        myConfig = SkemaPackConfig( codecs.open( "testSpecialChars.cfg", 'r', 'utf-8' ) )
        Events, config = ImportFile( myConfig, ConfigSet = "ImportSpecialChars" ) #@UnusedVariable
        ExportFile(Events, myConfig, ConfigSet = "ExportSpecialChars" )
        #self.assertTrue( filecmp.cmp( ExportfileResultFile, ExportFileWeeksumKnownResult, shallow=False ) )
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()