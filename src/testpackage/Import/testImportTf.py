'''
Created on 4 Apr 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig

from Import.ImportTf import ImportTf


ImportTfZipWorkDir = "ImportTf"
ImportTfZipCfgFilename = "ImportTf.cfg"

#FilesInZip = [ "Kopi af IT budget 2012.xlsx", "TFopsum_2012_ver0_0HHAL.xls",
#              "Timefag_E2012_ver0_0HHAL.xls", "Timefag_F2012_ver1_0hhal.xls",
#              "Timefag_F2013_ver0_0hhal.xls" ]
#
#ZipDataDir = "ziptemp/"
TfKnownResultLength = 321
TfKnownResultFirstEntry = {'Week': 35, 'Class': u'1. Sem A Elektronik', 
                           'LessonCount': 9, 'Year': 2012, 
                           'Teacher': u'Teacher1', 'Subject': u'Subject A1'} 

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

    def testBasicConstruction(self):
        ''' ImportTf : simple TF construction test '''
        events, config = ImportTf( self.myConfig ) #@UnusedVariable
        self.assertEqual(len(events), TfKnownResultLength )
        self.assertEqual( events[0],TfKnownResultFirstEntry  )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()