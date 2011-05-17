#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on May 15, 2011

@author: morten
'''

# handling pythonpath
import sys, os

this_dir = os.path.abspath(__file__)
while 1 == 1:
    this_dir, tail = os.path.split(this_dir)
    if tail == 'src': # always go to src as default dir.
        this_dir = os.path.join(this_dir, tail) 
        break
sys.path.append(this_dir) 
print "Added %s to PYTHONPATH" % this_dir

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
            print "%d Student %s" % (i, StudentList[i]['Name'] )
            outfile.write( StudentList[i]['Name'].encode('utf-8'))
            for HandinName in sorted( StudentHandins.iterkeys() ):
                outfile.write( "\t%s"% StudentHandins[HandinName])
            outfile.write( "\n")
        else:
            print "%d Student %s skipped" % (i, StudentList[i]['Name'] )

        i = i + 1
        
    print "done"
        