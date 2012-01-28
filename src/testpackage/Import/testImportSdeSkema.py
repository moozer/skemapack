'''
Created on 27 Jan 2012

@author: moz
'''
import unittest
from Import.ImportSdeSkema import ImportSdeSkema
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
from Datatypes.EventFunctions import WriteEvents, ReadEvent, MakeEventString


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


    def testReadHtmlFromFile(self):
        ''' ImportSdeSkema : Test reading from file (as opposed to the net)'''
        events =  ImportSdeSkema( self.myConfig, ConfigSet = CfgSet )
        # WriteEvents(events, self.myConfig, CfgSet )
        KnownResult = ImportFile( self.myConfig )
        
        self.assertEqual(len(events), len(KnownResult) )
        
        for i in range( 0, len(events) ):
            self.assertEqual( events[i], KnownResult[i] )
        
        pass




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
