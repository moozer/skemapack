'''
Created on 26 May 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
from Filter.FilterSplit import FilterSplit
import datetime

FilterSplitWorkDir = "FilterSplit"
FilterSplitCfgFilename = "FilterSplit.cfg"
KnownFilteredEvents = [
    {'Class': '11OIT3bH2', 'Hours': [datetime.datetime(2011, 8, 22, 8, 30), datetime.datetime(2011, 8, 22, 9, 15)], 'Location': 'b-1.44', 'Date': datetime.date(2011, 8, 22), 'Teacher': 'mon2', 'Subject': 'Adv. networking'},   
    {'Class': '11OIT3bH2', 'Hours': [datetime.datetime(2011, 8, 22, 10, 20), datetime.datetime(2011, 8, 22, 11, 5)], 'Location': 'b-1.44', 'Date': datetime.date(2011, 8, 22), 'Teacher': 'mon2', 'Subject': 'Adv. networking'},    
    {'Class': '11OIT3bH2', 'Hours': [datetime.datetime(2011, 8, 23, 8, 30), datetime.datetime(2011, 8, 23, 9, 15)], 'Location': 'b-1.44', 'Date': datetime.date(2011, 8, 23), 'Teacher': 'mon2', 'Subject': 'IT Security'},    
    {'Class': '11OIT3bH2', 'Hours': [datetime.datetime(2011, 8, 23, 9, 15), datetime.datetime(2011, 8, 23, 10, 0)], 'Location': 'b-1.44', 'Date': datetime.date(2011, 8, 23), 'Teacher': 'mon2', 'Subject': 'IT Security'},    
    {'Class': '11OIT3bH2', 'Hours': [datetime.datetime(2011, 8, 23, 10, 20), datetime.datetime(2011, 8, 23, 11, 5)], 'Location': 'b-1.44', 'Date': datetime.date(2011, 8, 26), 'Teacher': 'mon2', 'Subject': 'IT Security'},    
    {'Class': '11OIT3bH2', 'Hours': [datetime.datetime(2011, 8, 26, 8, 30), datetime.datetime(2011, 8, 26, 9, 15)], 'Location': 'b-1.44', 'Date': datetime.date(2011, 8, 26), 'Teacher': 'mon2', 'Subject': 'IT Security'},
    {'Class': '11OIT3bH2', 'Hours': [datetime.datetime(2011, 8, 29, 11, 5), datetime.datetime(2011, 8, 29, 11, 50)], 'Location': 'b-1.44', 'Date': datetime.date(2011, 9, 1), 'Teacher': 'mon2', 'Subject': 'IT Security'} ]   

KnownFilteredWeeksums = [
    {'Week': 34, 'Class': '11OIT3bH2', 'LessonCount': 4, 'Year': 2011, 'Teacher': 'mon2', 'Subject': 'Adv. networking'},
    {'Week': 35, 'Class': '11OIT3bH2', 'LessonCount': 2, 'Year': 2011, 'Teacher': 'mon2', 'Subject': 'Adv. networking'} 
    ]   

class Test(unittest.TestCase):
    
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( FilterSplitWorkDir)
        
        self.myConfig = SkemaPackConfig( open( FilterSplitCfgFilename ) )
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass


    def testBasicOneTeacherEventFiltering(self):
        events, config = ImportFile( self.myConfig )
        FilteredEvents, config = FilterSplit( events, config, ConfigSet="FilterSplitEvents" )
        
        self.assertEqual(FilteredEvents, KnownFilteredEvents )
        pass

    def testBasicOneTeacherWeeksumsFiltering(self):
        events, config = ImportFile( self.myConfig, ConfigSet = "ImportFileWeeksums" )
        FilteredWeeksums, config = FilterSplit( events, config, ConfigSet="FilterSplitWeeksums" )
        
        self.assertEqual(FilteredWeeksums, KnownFilteredWeeksums )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()