# -*- coding: UTF-8 -*-


'''
Created on Oct 15, 2010

    Imports all unit tests from the test package

@author: pfl
'''
import unittest

from testpackage.Input.testHtmlGetter.testHtmlGetter import Test as testHtmlGetter
#
from testpackage.Input.testHtmlScraper import *
from testpackage.Input.testHtmlScraper.TestBeautifulSoupScraper import TestInstantiations as testHtmlScraper

if __name__ == "__main__":
    unittest.main()
