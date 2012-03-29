'''
Created on 10 Feb 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Output.HtmlTableOutput import HtmlTableOutput

WorkDir = 'ExportHtml'
Weeksums = [{'Week': 34, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 34, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 35, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011}, 
             {'Week': 35, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011}]

ResultHtml = '''<table>\n\t<tr><td>Class</td><td>Subject</td><td>2011-34</td><td>2011-35</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td></tr>
</table>
'''

ResultHtmlWithRowSums = '''<table>\n\t<tr><td>Class</td><td>Subject</td><td>2011-34</td><td>2011-35</td><td>Sum</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td><td>6</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td><td>8</td></tr>
</table>
'''

ResultHtmlWithColSums = '''<table>\n\t<tr><td>Class</td><td>Subject</td><td>2011-34</td><td>2011-35</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td></tr>
\t<tr><td></td><td></td><td>9</td><td>5</td></tr>
</table>
'''

ResultHtmlWithRowAndColSums = '''<table>\n\t<tr><td>Class</td><td>Subject</td><td>2011-34</td><td>2011-35</td><td>Sum</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td><td>6</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td><td>8</td></tr>
\t<tr><td></td><td></td><td>9</td><td>5</td><td>14</td></tr>
</table>
'''


IcsFilename = 'ExportIcsResult.ics'
IcsKnownResultFile = 'ExportIcsKnownResult.ics'

class Test(unittest.TestCase):
    def setUp(self):
        CloneTestData() 
        self._StartDir = ChDirToSrc()
        os.chdir(TempDataDir)
        os.chdir( WorkDir)
        pass

    def tearDown(self):
        ''' Removes temporary data '''
        RemoveTestData()        
        os.chdir(self._StartDir )
        pass

    def testBasicTableoutput(self):
        ''' HtmlTableOutput : basic output '''
        Html = HtmlTableOutput( Weeksums )
        self.assertEqual( ResultHtml, Html )
        pass
    
    def testTableWithRowSums(self):
        ''' HtmlTableOutput : table with Row sums '''
        Html = HtmlTableOutput( Weeksums, RowSums = True )
        self.assertEqual( ResultHtmlWithRowSums, Html )
        pass
    
    def testTableWithColSums(self):
        ''' HtmlTableOutput : table with Column sums '''
        Html = HtmlTableOutput( Weeksums, ColSums = True )
        self.assertEqual( ResultHtmlWithColSums, Html )
        pass
    
    def testTableWithRowAndColSums(self):
        ''' HtmlTableOutput : table with both row and column sums '''
        Html = HtmlTableOutput( Weeksums, ColSums = True, RowSums = True )
        self.assertEqual( ResultHtmlWithRowAndColSums, Html )
        pass
  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
  
    