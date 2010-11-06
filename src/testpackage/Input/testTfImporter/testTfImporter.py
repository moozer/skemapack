# -*- coding: UTF-8 -*-
'''
Testing basic tf import
@author: mon
'''
import unittest
import Input.TfImporter.TfCsvImport.TfCsvImport as TfCsvImport

# Test data
TfInputCsvFile = "testdata/TF_skema.csv"

class Test(unittest.TestCase):

    def testConstruction(self):
        ''' test construction of TfCsvImport '''
        tfi = TfCsvImport(TfInputCsvFile )
        self.assertEqual( tfi.getCsvFilename() == TfInputCsvFile )
#    def testReadFromCsv(self):
#        ''' TfImport : '''
#        myLoader = loadWeb.htmlGetter()
#        self._htmlResponse = myLoader.getSkemaWithPost(3735, 43, 43)
#        parser = BeautifulSkemaScraper(DateFormat = "%d-%m-%Y")
#        parser.feed( self._htmlResponse.read() )
#        parser.close()
#        i = len(parser.Appointments)
#        self.assertEqual(i,19)
#        pass
#    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()