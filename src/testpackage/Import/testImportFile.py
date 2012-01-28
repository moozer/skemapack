'''
Created on 28 Jan 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
import datetime


ImportFileWorkDir = 'ImportFile'
ImportFileCfgFilename = 'ImportFile.cfg'

ImportFileData = [   {'Date': datetime.datetime(2011, 8, 22, 0, 0), 
     'Hours': (datetime.datetime(2011, 8, 22, 8, 30), 
               datetime.datetime(2011, 8, 22, 9, 15)), 
     'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 22, 0, 0), 
     'Hours': (datetime.datetime(2011, 8, 22, 9, 15), 
               datetime.datetime(2011, 8, 22, 10, 0)), 
     'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 22, 0, 0), 
     'Hours': (datetime.datetime(2011, 8, 22, 10, 20), 
               datetime.datetime(2011, 8, 22, 11, 5)), 
     'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 23, 0, 0), 
     'Hours': (datetime.datetime(2011, 8, 22, 11, 5), 
               datetime.datetime(2011, 8, 22, 11, 50)), 
     'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 23, 0, 0), 
     'Hours': (datetime.datetime(2011, 8, 23, 8, 30), 
               datetime.datetime(2011, 8, 23, 9, 15)), 
     'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 23, 0, 0), 
     'Hours': (datetime.datetime(2011, 8, 23, 9, 15), 
               datetime.datetime(2011, 8, 23, 10, 0)), 
     'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'},
    {'Date': datetime.datetime(2011, 8, 26, 0, 0), 
     'Hours': (datetime.datetime(2011, 8, 23, 10, 20), 
               datetime.datetime(2011, 8, 23, 11, 5)), 
     'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 26, 0, 0), 'Hours': (datetime.datetime(2011, 8, 26, 8, 30), datetime.datetime(2011, 8, 26, 9, 15)), 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 26, 0, 0), 'Hours': (datetime.datetime(2011, 8, 26, 9, 15), datetime.datetime(2011, 8, 26, 10, 0)), 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': (datetime.datetime(2011, 8, 26, 10, 20), datetime.datetime(2011, 8, 26, 11, 5)), 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': (datetime.datetime(2011, 8, 29, 8, 30), datetime.datetime(2011, 8, 29, 9, 15)), 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': (datetime.datetime(2011, 8, 29, 9, 15), datetime.datetime(2011, 8, 29, 10, 0)), 'Subject': 'Adv. networking', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 8, 29, 0, 0), 'Hours': (datetime.datetime(2011, 8, 29, 10, 20), datetime.datetime(2011, 8, 29, 11, 5)), 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}, 
    {'Date': datetime.datetime(2011, 9, 1, 0, 0), 'Hours': (datetime.datetime(2011, 8, 29, 11, 5), datetime.datetime(2011, 8, 29, 11, 50)), 'Subject': 'IT Security', 'Location': 'b-1.44', 'Class': '11OIT3bH2'}];


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
        ''' ImportFile : basic test of inpur capability '''
        events = ImportFile( self.myConfig )
        self.assertEqual( events, ImportFileData )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()