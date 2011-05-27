# -*- coding: utf-8 -*-
'''
Created on Nov 7, 2010

@author: morten
'''
import unittest
from Output.TableOutput.TableOutput import TableOutput
from Datatypes.ActivityData import ActivityData

from testpackage.Utilities.TestdataSupport.TableOutput import * #@UnusedWildImport

# test data

class Test(unittest.TestCase):
    def testConstruction(self):
        ''' TableOutput : constructs the TableOutput class '''
        TableOutput( IterableObject )
        pass

    def testGetTextile(self):
        ''' TableOutput : test building the textile table '''
        TO = TableOutput( IterableObject )
        Result = TO.GetTextileTable()
        self.assertEqual( Result, ObjectAsTextile )

    def testGetTextileNoHeader(self):
        ''' TableOutput : test building the textile table without headers '''
        TO = TableOutput( IterableObject, IncludeHeader=False )
        Result = TO.GetTextileTable()        
        self.assertEqual( Result, ObjectAsTextileNoHeader )

    def testGetTextileWithCSums(self):
        ''' TableOutput : test building the textile table with column sums'''
        TO = TableOutput( IterableObject, IncludeColumnSums=True )
        Result = TO.GetTextileTable()        
        self.assertEqual( Result, ObjectAsTextileColumnSum )

    def testGetTextileWithRSums(self):
        ''' TableOutput : test building the textile table with Row sums'''
        TO = TableOutput( IterableObject, IncludeRowSums=True )
        Result = TO.GetTextileTable()        
        self.assertEqual( Result, ObjectAsTextileRowSum )

    def testGetTextileWithRAndCSums(self):
        ''' TableOutput : test building the textile table with Row and column sums'''
        TO = TableOutput( IterableObject, IncludeRowSums=True, IncludeColumnSums=True )
        Result = TO.GetTextileTable()        
        self.assertEqual( Result, ObjectAsTextileRowAndColumnSum )

    def testGetTextileWithPreparation(self):
        ''' TableOutput : test building the textile table with Row and column sums and preparation'''
        TO = TableOutput( IterableObjectEasy, IncludeRowSums=True, IncludeColumnSums=True, 
                          IncludePreperation=True )
        Result = TO.GetTextileTable( StartWeek=1, EndWeek=3 )        
        self.assertEqual( Result, ObjectAsTextilePreparation )
                
# TODO: auto extraction of weeks would be nice
#    def testExtractWeeksFromData(self):
#        ''' TableOutput : test using weeks from ItObject '''
#        TO = TableOutput( IterableObject, AutoWeeks=True )
#        Result = TO.GetTextileTable()        
#        self.assertEqual( Result, ObjectAsTextile )
#        self.assertEqual( TO.GetWeeks(), WeeksInObject )
        
    def testGetHtml(self):
        ''' TableOutput : test the output converted to HTML '''
        TO = TableOutput( IterableObject )
        HTML = TO.GetHtmlTable()
        self.assertEqual( HTML, ObjectAsHtml )
        
    def testGetTextileWithExtra(self):
        ''' TableOutput : test building the textile table with extra iterator '''
        TO = TableOutput( IterableObject, ItObjectExtra=IterableObjectExtra1 )
        Result = TO.GetTextileTable()
        self.assertEqual( Result, ObjectAsTextileExtra1 )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    

    