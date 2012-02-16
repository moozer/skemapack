'''
Created on 7 Feb 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
#from Export.ExportFile import ExportFile
from Convert.ConvertToWeeksum import ConvertToWeeksum
from testpackage.Utilities.TestdataSupport.WeeksumData import * 

ImportFileWorkDir = 'ImportFile'
ImportFileCfgFilename = 'ImportFile.cfg'


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

    def testSimpleConvert(self):
        ''' ConvertToWeeksum : basic init '''
        events = ImportFile( self.myConfig )
        Sum = ConvertToWeeksum( events, self.myConfig )
        self.assertEqual(Sum, ImportFileTestDataSum )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()