'''
Created on 27 Jan 2012

@author: moz
'''
import unittest
from Import.ImportSdeSkema import ImportSdeSkema
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin

CfgFilename = 'BasicSdeSkemaImportFromFile.cfg'
EventsInFile = 38
CfgSet = 'SkemaScraperFromFile'

class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( 'ImportSdeSkema')
        
        self.myConfig = SkemaPackConfig( open( CfgFilename ) )
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass


    def testReadFromFile(self):
        ''' ImportSdeSkema : Test reading from file (as opposed to the net)'''
        events =  ImportSdeSkema( self.myConfig, ConfigSet = CfgSet )
        self.assertEqual( len(events), EventsInFile )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()