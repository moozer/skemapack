'''
Created on 28 Jan 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Export.ExportIcs import ExportIcs
from Import.ImportFile import ImportFile

ImportFileWorkDir = 'ExportIcs'
ImportFileCfgFilename = 'ExportIcs.cfg'

IcsFilename = 'ExportIcsResult.ics'
IcsKnownResultFile = 'ExportIcsKnownResult.ics'

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


    def testKnownEventExport(self):
        ''' ExportIcs : exporting known entries '''
        events = ImportFile( self.myConfig )
        ExportIcs( events, self.myConfig )
        
        ret = os.system( 'diff %s %s ' % (IcsFilename, IcsKnownResultFile ))
        self.assertEqual( ret, 0 )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()