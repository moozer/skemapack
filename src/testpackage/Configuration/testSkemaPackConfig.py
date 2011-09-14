'''
Created on Sep 14, 2011

@author: flindt
'''
import unittest
from Configuration.SkemaPackConfig import SkemaPackConfig
import os

class Test(unittest.TestCase):


    def testLoadFromFile(self):
        self.config = SkemaPackConfig('config_test.cfg')
        self.assertEquals(self.config._ConfigParser.get("SkemaScraper", "TeacherId"), "5421", "TeacherId is not correct")
        self.assertEquals(self.config._ConfigParser.get("SkemaScraper", "FirstWeek"), "33", "FirstWeek is not correct")
        self.assertEquals(self.config._ConfigParser.get("SkemaScraper", "LastWeek"), "52", "LastWeek is not correct")
        self.assertEquals(self.config._ConfigParser.get("SkemaScraper", "Year"), "2011", "Year is not correct")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoadFromFile']
    unittest.main()