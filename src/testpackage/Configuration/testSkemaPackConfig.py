'''
Created on Sep 14, 2011

@author: flindt
'''
import unittest
from Configuration.SkemaPackConfig import SkemaPackConfig
import os
import exceptions
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport

ConfigWorkDir = 'Configuration'

ConfigStringResult = '''# [SkemaScraper]
# teacherid = 5421
# firstweek = 33
# lastweek = 52
# year = 2011
# dateformat = %d-%m-%Y
#
'''

class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( ConfigWorkDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass
    
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
    
    @unittest.skip("(MON) How is this working?")    
    def testLoadFromCurrent(self):
        os.system("cp config_test.cfg skemapack.cfg")
        self.config = SkemaPackConfig()
        self.assertEquals(self.config.get("SkemaScraper", "TeacherId"), "5421", "TeacherId is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "FirstWeek"), "33", "FirstWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "LastWeek"), "52", "LastWeek is not correct")
        self.assertEquals(self.config.get("SkemaScraper", "Year"), "2011", "Year is not correct")
        os.system("rm skemapack.cfg")
        
    @unittest.skip("(MON) How is this working?")    
    def testLoadNoFile(self):
        HomeFileName = os.path.expanduser("~/.skemapack/skemapack.cfg")
        os.system("mv %s %s.old"%(HomeFileName,HomeFileName))
        print "mv %s %s.old"%(HomeFileName,HomeFileName)
        self.assertRaises( exceptions.ValueError, SkemaPackConfig, "" )
        os.system("mv %s.old %s"%(HomeFileName,HomeFileName))
        
    #@unittest.skip("Skipped : Errors related to file locations")    
    def testPrintConfig(self):
        ''' SkemaPackConfig : check output string '''
        self.config = SkemaPackConfig(open('config_test.cfg'))
        configstr = str( self.config )
        self.assertEqual( configstr, ConfigStringResult )

    def testTrueFalseConfig(self):
        ''' SkemaPackConfig : simple read of true/false'''
        self.config = SkemaPackConfig(open('TrueFalseTest.cfg'))
        self.assertEquals(self.config.getboolean("TrueFalseTest", "ThisIsTrue"), True )
        self.assertEquals(self.config.getboolean("TrueFalseTest", "ThisIsFalse"), False )

    def testSetGet(self):
        ''' SkemaPackConfig : simple set and read of value'''
        self.config = SkemaPackConfig(open('config_test.cfg'))
        
        SectionToUse =  "SkemaScraper"
        OptionToUse = "MyVal"
        ValueToUse = "Test123"
        self.config.set( SectionToUse, OptionToUse, ValueToUse )
         
        self.assertEquals(self.config.get(SectionToUse, OptionToUse), ValueToUse )

    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoadFromFile']
    unittest.main()