'''
Created on Mar 29, 2012

@author: flindt
'''
import unittest

from Input.DumpCsv import DumpCsvFromXml
 

class Test(unittest.TestCase):


    def testNoInput(self):
        XmlFileName = None 
        CsvFileName = None
        SheetName = None
        Seperator = None
        DumpCsvFromXml.DumpNamedSheet( XmlFileName, CsvFileName, SheetName, Seperator)
        pass





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()