#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on May 15, 2011

@author: morten
'''

# handling pythonpath
from PythonPathUtil import AppendSrcToPythonPath
AppendSrcToPythonPath()

from optparse import OptionParser
from Input.FronterPortfolio.FronterPortfolio import FronterPortfolio

def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile", 
                      help="File to read html data from", metavar="INFILE")
    parser.add_option("-o", "--outfile", dest="outfile", default="portfolio.csv",
                      help="Filename of output file", metavar="OUTFILE")        
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options

if __name__ == '__main__':
    opt = ParseCmdLineOptions()    

    print "Opening html file: %s" % opt.infile
    fp = FronterPortfolio( opt.infile )
    
    print "Opening outputfile %s" % opt.outfile
    outfile = open( opt.outfile, "w+")
    
    print "output header line"
    outfile.write( "Student name" )
    for Handin in sorted( fp.getHandinTitle() ):
        outfile.write( "\t%s" % Handin)
    outfile.write("\n")
    
    print "output one line per student"
    StudentList = fp.getStudentNames()
    
    i = 0
    for StudentHandins in fp.getHandinsByStudent():
        if StudentList[i]['Include']:
            CourseList = {}
            
            print "%d Student %s" % (i, StudentList[i]['Name'] )
            outfile.write( StudentList[i]['Name'].encode('utf-8'))
            for HandinName in sorted( StudentHandins.iterkeys() ):
                sh = StudentHandins[HandinName]
                if sh['Course'] in CourseList:
                    CourseList[sh['Course']]['Count'] += 1
                    CourseList[sh['Course']]['Missing'] |= sh['Missing']
                    CourseList[sh['Course']]['Pending'] |= sh['Pending']
                else:
                    CourseList[sh['Course']]= {}
                    CourseList[sh['Course']]['Count'] = 1
                    CourseList[sh['Course']]['Missing'] = sh['Missing']
                    CourseList[sh['Course']]['Pending'] = sh['Pending']
                    
                outfile.write( "\t%s"% sh['Evaluation'])
                
            GlobalSum = {'Missing': False, 'Pending': False }
            for Course in CourseList:
                outfile.write( "\t%s%s" % ('Missing' if CourseList[Course]['Missing'] else 'Ok', 
                                            '/Pending' if CourseList[Course]['Pending'] else  '' ))
                GlobalSum['Missing'] |= CourseList[Course]['Missing']
                GlobalSum['Pending'] |= CourseList[Course]['Pending']
                
            
            outfile.write( "\t%s%s" % ('Missing' if GlobalSum['Missing'] else 'Ok', 
                                       '/Pending' if GlobalSum['Pending'] else  '' ))
            outfile.write( "\t%s" % StudentList[i]['Name'].encode('utf-8')) 
            outfile.write( "\n")
        else:
            print "%d Student %s skipped" % (i, StudentList[i]['Name'] )

        i = i + 1
    
    # @TODO header at the end ...
    print "output header line"
    outfile.write( "Student name" )
    for Handin in sorted( fp.getHandinTitle() ):
        outfile.write( "\t%s" % Handin)
    for Course in CourseList:
        outfile.write( "\t%s (sum)" % (Course) ) 
    outfile.write( "\tTotal (sum)" )
    outfile.write( "\tStudent name" )
        
    outfile.write("\n")
    
    print "done"


