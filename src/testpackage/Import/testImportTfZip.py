'''
Created on 4 Apr 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig

from Import.ImportTfZip import ImportTfZip


ImportTfZipWorkDir = "ImportTfZip"
ImportTfZipCfgFilename = "ImportTfZip.cfg"

class Test(unittest.TestCase):

    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( ImportTfZipWorkDir)
        
        self.myConfig = SkemaPackConfig( open( ImportTfZipCfgFilename ) )
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testBasicUnzip(self):
        ''' ImportTfZip : simple unzip a check content '''
        events, config = ImportTfZip( self.myConfig, "ImportTfZip" )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()