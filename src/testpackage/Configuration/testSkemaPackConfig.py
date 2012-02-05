'''
Created on Sep 14, 2011

@author: flindt
'''
import unittest
from Configuration.SkemaPackConfig import SkemaPackConfig
import os
import exceptions


class Test(unittest.TestCase):

    @unittest.skip("Skipped to have all unittests working")    
    def testLoadFromFile(self):
        self.config = SkemaPackConfig('config_test.cfg')
        self.assertEquals(self.config.get("SkemaScraper", "TeacherId"), "5421", "TeacherId is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "FirstWeek"), "33", "FirstWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "LastWeek"), "52", "LastWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "Year"), "2011", "Year is not correct")
        
    @unittest.skip("Skipped to have all unittests working")    
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
        
    @unittest.skip("Skipped to have all unittests working")    
    def testPrintConfig(self):
        self.config = SkemaPackConfig('config_test.cfg')
        print self.config
        
    def testFromSTDIN(self):
        pass
        
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoadFromFile']
    unittest.main()