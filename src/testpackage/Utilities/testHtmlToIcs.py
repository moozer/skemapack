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
        self._StartDir = os.getcwd()
        this_dir = os.path.dirname( __file__ )
        while 1 == 1:
            this_dir, tail = os.path.split( this_dir )
            if tail == 'src': # always go to src as default dir.
                this_dir = os.path.join( this_dir, tail )
                break
        os.chdir( this_dir )
        
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
        ret = os.system('python2.7 %s --infile "%s" --outfile "%s" --date-format "%s" > /dev/null' % (HtmlToIcsFilename, HtmlFileToProcess, Outputfilename, "%d-%m-%Y") )
        self.assertEqual( ret, 0 )
        ret = os.system( 'diff %s %s  > /dev/null' % (IcsResultFile, Outputfilename ))
        self.assertEqual( ret, 0 )

    def testHtmlToIcs2010Week45(self):
        ''' HtmlToIcs : Collect week 45 (of 2010), and compare to known ics '''
        cmd = 'python2.7 %s --id %i --outfile "%s" --date-format "%s" --first-week 45 --end-week 45 --year 2010' % (HtmlToIcsFilename, SkemaId, Outputfilename, "%d-%m-%Y")
        ret = os.system( cmd + "> /dev/null" )
        self.assertEqual( ret, 0 )
        ret = os.system( 'diff %s %s  > /dev/null' % (Outputfilename, SkemaUrlResultIcs ))
        self.assertEqual( ret, 0 )
        
    def testHtmlToIcsCurrentWeek(self):
        ''' HtmlToIcs : Checking fetching of current week '''
        cmd = 'python2.7 %s --url "%s" --outfile "%s" --date-format "%s"' % (HtmlToIcsFilename, SkemaUrlToUse, Outputfilename, "%d-%m-%Y")
        ret = os.system( cmd + "> /dev/null" )
        self.assertEqual( ret, 0 )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()