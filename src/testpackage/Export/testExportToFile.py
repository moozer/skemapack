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

# using the same vars as testImportFile

ExportFileTestFileName = "teststdout.txt"

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
        Events = ImportFile(self.myConfig, 'ImportExportedFile')
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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()