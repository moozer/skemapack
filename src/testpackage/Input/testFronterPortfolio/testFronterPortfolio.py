'''
Created on May 15, 2011

@author: morten
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport

from Input.FronterPortfolio.FronterPortfolio import * #@UnusedWildImport
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
        
    def testGetHandinTitles(self):
        fp = FronterPortfolio( PortfolioFilename )
        res =  fp.getHandinTitle() 
        self.assertEqual( PortfolioHandins, res )
        
    def testGetHandinsByStudent(self):
        fp = FronterPortfolio( PortfolioFilename )
        res =  fp.getHandinsByStudent() 
        
        i = 0
        Result = []
        for StudentHandins in res:
            Result.append( StudentHandins )
            i = i+1
            if i == 3:
                break

        self.assertEqual( PortfolioHandinsFirstStudent, Result[0] )
        self.assertEqual( PortfolioHandinsSecondStudent, Result[1] )
        self.assertEqual( PortfolioHandinsThirdStudent, Result[2] )
            
        
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReadFromFile']
    unittest.main()