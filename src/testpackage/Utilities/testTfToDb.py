'''
Created on May 7, 2011

@author: morten
'''
import unittest, os

TempDataDir="tempdata"
TfFile = "TfToHtmlWithExtra/TF_skema.csv"
TfExtraFile = "TfToHtmlWithExtra/TF_extra_1.csv"
Outputfilename = "tftodbtest.sqlite"
TfToDbFilename= "../../../Utilities/TfToDb.py"
BaseDbFile = "TfToDb/BaseDb.sql"

PythonBinaryToUse = "python2.7"

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

    def testTfToDb(self):
        ''' TfToHtml : compares known skema HTML input with known HTML output '''
        CmdString = '%s %s --infile "%s" -x "%s" --outfile "%s" --basedb "%s"' \
                    % (PythonBinaryToUse, TfToDbFilename, TfFile, TfExtraFile, Outputfilename, BaseDbFile )
        ret = os.system( CmdString )
        self.assertEqual( ret, 0 )
#        ret = os.system( 'diff %s %s  > /dev/null' % (HtmlResultFile, Outputfilename ))
#        #ret = os.system( 'diff %s %s ' % (HtmlResultFile, Outputfilename ))
#        self.assertEqual( ret, 0 )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()