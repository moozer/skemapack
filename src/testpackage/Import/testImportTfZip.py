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

FilesInZip = [ "Kopi af IT budget 2012.xlsx", "TFopsum_2012_ver0_0HHAL.xls",
              "Timefag_E2012_ver0_0HHAL.xls", "Timefag_F2012_ver1_0hhal.xls",
              "Timefag_F2013_ver0_0hhal.xls" ]

ZipDataDir = "ziptemp/"

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
        
        for FileName in FilesInZip:
            self.assertTrue( os.path.exists( ZipDataDir + FileName), "%s not found"%FileName )
        
        print events
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()