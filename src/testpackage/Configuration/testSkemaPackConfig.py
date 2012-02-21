'''
Created on Sep 14, 2011

@author: flindt
'''
import unittest
from Configuration.SkemaPackConfig import SkemaPackConfig
import os
import exceptions

ConfigStringResult = '''# [SkemaScraper]
# teacherid = 5421
# firstweek = 33
# lastweek = 52
# year = 2011
# dateformat = %d-%m-%Y
#
'''

class Test(unittest.TestCase):

    def testLoadFromFile(self):
        ''' SkemaPackConfig : simple read '''
        self.config = SkemaPackConfig(open('config_test.cfg'))
        self.assertEquals(self.config.get("SkemaScraper", "TeacherId"), "5421", "TeacherId is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "FirstWeek"), "33", "FirstWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "LastWeek"), "52", "LastWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "Year"), "2011", "Year is not correct")
        
    @unittest.skip("Skipped : (MON) How should this work?")    
    def testLoadFromHome(self):
        self.config = SkemaPackConfig()
        self.assertEquals(self.config.get("SkemaScraper", "TeacherId"), "5421", "TeacherId is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "FirstWeek"), "33", "FirstWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "LastWeek"), "52", "LastWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "Year"), "2011", "Year is not correct")
    
    @unittest.skip("Skipped to have all unittests working")    
    def testLoadFromCurrent(self):
        os.system("cp config_test.cfg skemapack.cfg")
        self.config = SkemaPackConfig()
        self.assertEquals(self.config.get("SkemaScraper", "TeacherId"), "5421", "TeacherId is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "FirstWeek"), "33", "FirstWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "LastWeek"), "52", "LastWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "Year"), "2011", "Year is not correct")
        os.system("rm skemapack.cfg")
        
    @unittest.skip("Skipped to have all unittests working")    
    def testLoadNoFile(self):
        HomeFileName = os.path.expanduser("~/.skemapack/skemapack.cfg")
        os.system("mv %s %s.old"%(HomeFileName,HomeFileName))
        print "mv %s %s.old"%(HomeFileName,HomeFileName)
        self.assertRaises( exceptions.ValueError, SkemaPackConfig, "" )
        os.system("mv %s.old %s"%(HomeFileName,HomeFileName))
        
    def testPrintConfig(self):
        ''' SkemaPackConfig : check output string '''
        self.config = SkemaPackConfig(open('config_test.cfg'))
        configstr = str( self.config )
        self.assertEqual( configstr, ConfigStringResult )
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoadFromFile']
    unittest.main()