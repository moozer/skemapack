'''
Created on Nov 11, 2010

@author: morten
'''
import unittest
import os

HtmlToIcsFilename= "../../../Utilities/HtmlToIcs.py"
TempDataDir="tempdata"
HtmlFileToProcess = "HtmlFromSkema/laererSkema.aspx_29-52.html"
IcsResultFile = "HtmlFromSkema/laererSkema.aspx_29-52.ics"
Outputfilename = "testResult.ics"

# test one week
SkemaUrlToUse = "http://skema.sde.dk/laererSkema.aspx?idx=5421&lang=da-DK"
SkemaUrlResultIcs = "SkemaMon/SkemaMon2010Week45.ics"

SkemaId = 5421


class Test(unittest.TestCase):
    ''' Testing HtmlToIcs from an external shell like perspective '''
    def setUp(self):
        ''' makes a copy of the test data to avoid overwriting something '''
        self._StartDir = os.getcwd()
        try: # if it fails, then we are in the correct directory.
            os.chdir("testpackage/Utilities")
        except:
            pass
        
        if os.system('sh CloneTestData.sh'):
            raise IOError( "CloneTestData.sh not found in %s" % os.getcwd())

        # every work from temp data dir.
        os.chdir(TempDataDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        os.chdir(self._StartDir )
        try: # if it fails, then we are in the correct directory.
            os.chdir("testpackage/Utilities")
        except:
            pass
        os.system('sh RemoveTestData.sh')
        os.chdir(self._StartDir )
        pass

    def testHtmlToIcsWithDatestring(self):
        ''' HtmlToIcs : compares known skema HTML input with known ICS output '''
        ret = os.system('python %s --infile "%s" --outfile "%s" --date-format "%s" > /dev/null' % (HtmlToIcsFilename, HtmlFileToProcess, Outputfilename, "%d-%m-%Y") )
        self.assertEqual( ret, 0 )
        ret = os.system( 'diff %s %s  > /dev/null' % (IcsResultFile, Outputfilename ))
        self.assertEqual( ret, 0 )

    def testHtmlToIcs2010Week45(self):
        ''' HtmlToIcs : Collect week 45 (of 2010), and compare to known ics '''
        cmd = 'python %s --id %i --outfile "%s" --date-format "%s" --first-week 45 --end-week 45' % (HtmlToIcsFilename, SkemaId, Outputfilename, "%d-%m-%Y")
        ret = os.system( cmd  ) #+ "> /dev/null" )
        self.assertEqual( ret, 0 )
        ret = os.system( 'diff %s %s  > /dev/null' % (Outputfilename, SkemaUrlResultIcs ))
        self.assertEqual( ret, 0 )
        
    def testHtmlToIcsCurrentWeek(self):
        ''' HtmlToIcs : Checking fetching of current week '''
        cmd = 'python %s --url "%s" --outfile "%s" --date-format "%s"' % (HtmlToIcsFilename, SkemaUrlToUse, Outputfilename, "%d-%m-%Y")
        ret = os.system( cmd + "> /dev/null" )
        self.assertEqual( ret, 0 )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()