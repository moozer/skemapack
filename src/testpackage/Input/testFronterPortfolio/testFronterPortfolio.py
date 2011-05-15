'''
Created on May 15, 2011

@author: morten
'''
import unittest
from testpackage.Utilities.SupportStuff import *

from Input.FronterPortfolio.FronterPortfolio import *
from testpackage.Utilities.TestdataSupport.FronterPortfolio import *

class Test(unittest.TestCase):

    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass
   
    def testReadFromFile(self):
        fp = FronterPortfolio( PortfolioFilename )
        self.assertEqual( fp.getFilename(), PortfolioFilename )

    def testGetStudentnames(self):
        fp = FronterPortfolio( PortfolioFilename )
        res =  fp.getStudentNames() 
        self.assertEqual( PortfolioStudents, res )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReadFromFile']
    unittest.main()