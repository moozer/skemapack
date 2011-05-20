#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on May 7, 2011

@author: morten
'''
import unittest, os
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport

TfFile = "TfToHtmlWithExtra/TF_skema.csv"
TfExtraFile = "TfToHtmlWithExtra/TF_extra_1.csv"
Outputfilename = "tftodbtest.sqlite"
TfToDbFilename= "../../../Utilities/TfToDb.py"
BaseDbFile = "TfToDb/BaseDb.sql"

PythonBinaryToUse = "python"

class Test(unittest.TestCase):
    ''' Testing HtmlToIcs from an external shell like perspective '''
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