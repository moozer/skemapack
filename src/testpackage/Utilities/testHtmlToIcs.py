'''
Created on Nov 11, 2010

@author: morten
'''
import unittest
import os

HtmlToIcsFilename=os.getcwd() + "/../../Utilities/HtmlToIcs.py"
TempDataDir="tempdata"
HtmlFileToProcess = "HtmlFromSkema/laererSkema.aspx_29-52.html"
IcsResultFile = "HtmlFromSkema/laererSkema.aspx_29-52.ics"
Outputfilename = "testReasult.ics"

class Test(unittest.TestCase):
    ''' Testing HtmlToIcs from an external shell like perspective '''
    def setUp(self):
        ''' makes a copy of the test data to avoid overwriting something '''
        self._StartDir = os.getcwd()
        if os.system('sh CloneTestData.sh'):
            raise IOError
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        os.chdir(self._StartDir )
        os.system('sh RemoveTestData.sh')
        pass

    def testHtmlToIcsWithDatestring(self):
        os.chdir(TempDataDir)
        ret = os.system('python %s --infile %s --outfile %s --date-format %s > /dev/null' % (HtmlToIcsFilename, HtmlFileToProcess, Outputfilename, "%d-%m-%Y") )
        self.assertEqual( ret, 0 )
        ret = os.system( 'diff %s %s  > /dev/null' % (IcsResultFile, Outputfilename ))
        self.assertEqual( ret, 0 )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()