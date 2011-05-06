'''
Created on Mar 3, 2011

@author: morten
'''
import unittest, os

TfToHtmlFilename= "../../../Utilities/TfToHtml.py"
TempDataDir="tempdata"
TfFile = "TfToHtmlWithExtra/TF_skema.csv"
TfExtraFile = "TfToHtmlWithExtra/TF_extra_1.csv"
Outputfilename = "testResult.html"
HtmlResultFile = "TfToHtmlWithExtra/testResult.html"

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
        ''' TfToHtml : compares known skema HTML input with known HTML output '''
        CmdString = 'python %s --infile "%s" -x "%s" --outfile "%s" -s 1 -e 52 --teachers "Teacher 7" > /dev/null' \
                    % (TfToHtmlFilename, TfFile, TfExtraFile, Outputfilename )
        ret = os.system( CmdString )
        self.assertEqual( ret, 0 )
        #ret = os.system( 'diff %s %s  > /dev/null' % (HtmlResultFile, Outputfilename ))
        ret = os.system( 'diff %s %s ' % (HtmlResultFile, Outputfilename ))
        self.assertEqual( ret, 0 )



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()