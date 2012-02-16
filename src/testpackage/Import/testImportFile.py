'''
Created on 28 Jan 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
import datetime
import sys
from testpackage.Utilities.TestdataSupport.WeeksumData import * 

ImportFileWorkDir = 'ImportFile'
ImportFileCfgFilename = 'ImportFile.cfg'

ImportFileData = [   
    {'Date': datetime.datetime(2011, 8, 22, 0, 0), 'Hours': [datetime.datetime(2011, 8, 22, 8, 30),  datetime.datetime(2011, 8, 22, 9, 15)], 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 22, 0, 0), 'Hours': [datetime.datetime(2011, 8, 22, 9, 15),  datetime.datetime(2011, 8, 22, 10, 0)], 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 22, 0, 0), 'Hours': [datetime.datetime(2011, 8, 22, 10, 20), datetime.datetime(2011, 8, 22, 11, 5)], 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 23, 0, 0), 'Hours': [datetime.datetime(2011, 8, 22, 11, 5),  datetime.datetime(2011, 8, 22, 11, 50)], 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 23, 0, 0), 'Hours': [datetime.datetime(2011, 8, 23, 8, 30),  datetime.datetime(2011, 8, 23, 9, 15)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 23, 0, 0), 'Hours': [datetime.datetime(2011, 8, 23, 9, 15),  datetime.datetime(2011, 8, 23, 10, 0)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'},
    {'Date': datetime.datetime(2011, 8, 26, 0, 0), 'Hours': [datetime.datetime(2011, 8, 23, 10, 20), datetime.datetime(2011, 8, 23, 11, 5)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 26, 0, 0), 'Hours': [datetime.datetime(2011, 8, 26, 8, 30),  datetime.datetime(2011, 8, 26, 9, 15)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 26, 0, 0), 'Hours': [datetime.datetime(2011, 8, 26, 9, 15),  datetime.datetime(2011, 8, 26, 10, 0)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': [datetime.datetime(2011, 8, 26, 10, 20), datetime.datetime(2011, 8, 26, 11, 5)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': [datetime.datetime(2011, 8, 29, 8, 30),  datetime.datetime(2011, 8, 29, 9, 15)], 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': [datetime.datetime(2011, 8, 29, 9, 15),  datetime.datetime(2011, 8, 29, 10, 0)], 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': [datetime.datetime(2011, 8, 29, 10, 20), datetime.datetime(2011, 8, 29, 11, 5)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}, 
    {'Date': datetime.datetime(2011, 9, 1, 0, 0),  'Hours': [datetime.datetime(2011, 8, 29, 11, 5),  datetime.datetime(2011, 8, 29, 11, 50)], 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2', 'Teacher': 'mon'}];

ImportFileFailedStreamCfgFilename = 'ImportFileFailedStream.cfg'
ImportFileFailedStreamDataFilename  = 'ImportFileFailedStreamTestData.txt'
ImportFileFailedStreamDataNoEntries = 156

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


    def testBasicRead(self):
        ''' ImportFile : basic test of input capability '''
        events = ImportFile( self.myConfig )
        self.assertEqual( events, ImportFileData )
        pass
    
    def testConfigObjectNone(self):
        ''' ImportFile : test if importfile can handle None as config object '''
        old_stdin = sys.stdin
        fp = file( ImportFileFailedStreamDataFilename )
        sys.stdin = fp 
        e = ImportFile( None )
        sys.stdin = old_stdin
        fp.close()
        self.assertEqual( len(e), ImportFileFailedStreamDataNoEntries )
        pass

    def testImportWeeksums(self):
        ''' ImportFile : test if import file handles weeksums '''
        ws = ImportFile( self.myConfig, "ImportWeeksums" )
        self.assertEqual( ws, ImportFileTestDataSum )

    def testImportFailsOnNonexistentSection(self):
        ''' ImportFile : Test if ImportFile raises a KeyError error when section specified is not in file '''
        self.assertRaises(KeyError, ImportFile, self.myConfig, "ThisSectionDoesNotExist")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()