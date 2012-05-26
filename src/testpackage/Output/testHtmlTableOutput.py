'''
Created on 10 Feb 2012

@author: moz
'''
import unittest
from testpackage.Utilities.SupportStuff import * #@UnusedWildImport
from Output.HtmlTableOutput import HtmlTableOutput

WorkDir = 'ExportHtml'
Weeksums = [{'Week': 32, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 32, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 33, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}, 
             {'Week': 33, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2011, 'Teacher': 'mon'}]

Weeksums2Years = [{'Week': 2, 'LessonCount': 5, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2013, 'Teacher': 'mon'}, 
             {'Week': 2, 'LessonCount': 4, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2013, 'Teacher': 'mon'}, 
             {'Week': 51, 'LessonCount': 3, 'Subject': 'IT Security', 'Class': '11OIT3bH2', 'Year': 2012, 'Teacher': 'mon'}, 
             {'Week': 51, 'LessonCount': 2, 'Subject': 'Adv. networking', 'Class': '11OIT3bH2', 'Year': 2012, 'Teacher': 'mon'}]


ResultHtml = '''<table>
\t<tr><td>Class</td><td>Subject</td><td class="WeekHeader">2011-32</td><td class="WeekHeader">2011-33</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td></tr>
</table>
'''

ResultHtmlWithRowSums = '''<table>
\t<tr><td>Class</td><td>Subject</td><td class="WeekHeader">2011-32</td><td class="WeekHeader">2011-33</td><td>Sum</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td><td>6</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td><td>8</td></tr>
</table>
'''

ResultHtmlWithColSums = '''<table>
\t<tr><td>Class</td><td>Subject</td><td class="WeekHeader">2011-32</td><td class="WeekHeader">2011-33</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td></tr>
\t<tr><td></td><td></td><td>9</td><td>5</td></tr>
</table>
'''

ResultHtmlWithRowAndColSums = '''<table>
\t<tr><td>Class</td><td>Subject</td><td class="WeekHeader">2011-32</td><td class="WeekHeader">2011-33</td><td>Sum</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td><td>6</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td><td>8</td></tr>
\t<tr><td></td><td></td><td>9</td><td>5</td><td>14</td></tr>
</table>
'''

ResultHtmlWithRowAndColSums2Years = '''<table>
\t<tr><td>Class</td><td>Subject</td><td class="WeekHeader">2012-51</td><td class="WeekHeader">2012-52</td><td class="WeekHeader">2013-1</td><td class="WeekHeader">2013-2</td><td>Sum</td></tr>
\t<tr><td>11OIT3bH2</td><td>Adv. networking</td><td>2</td><td>.</td><td>.</td><td>4</td><td>6</td></tr>
\t<tr><td>11OIT3bH2</td><td>IT Security</td><td>3</td><td>.</td><td>.</td><td>5</td><td>8</td></tr>
\t<tr><td></td><td></td><td>5</td><td>.</td><td>.</td><td>9</td><td>14</td></tr>
</table>
'''





ResultHtmlWithTeacherClassSubject = '''<table>
\t<tr><td>Teacher</td><td>Class</td><td>Subject</td><td class="WeekHeader">2011-32</td><td class="WeekHeader">2011-33</td></tr>
\t<tr><td>mon</td><td>11OIT3bH2</td><td>Adv. networking</td><td>4</td><td>2</td></tr>
\t<tr><td>mon</td><td>11OIT3bH2</td><td>IT Security</td><td>5</td><td>3</td></tr>
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

    def testTableWithTeacherClassSubject(self):
        ''' HtmlTableOutput : table with teacher, class, and subject columns '''
        Html = HtmlTableOutput( Weeksums, ColSums = False, RowSums = False, Headers=["Teacher", "Class", "Subject"] )
        self.assertEqual( ResultHtmlWithTeacherClassSubject, Html )
        pass

    def testTableWithRowAndColSums_2Years(self):
        ''' HtmlTableOutput : table with both row and column sums '''
        Html = HtmlTableOutput( Weeksums2Years, ColSums = True, RowSums = True )
        self.assertEqual( ResultHtmlWithRowAndColSums2Years, Html )
        pass
  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
 
