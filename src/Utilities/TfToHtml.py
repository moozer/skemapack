#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2010

@author: morten
'''

from optparse import OptionParser
from Input.TfImporter.TfCsvImport import TfCsvImport
from Output.TableOutput.TableOutput import TableOutput

def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile", default = None,
                      help="Location of TF csv file to read", metavar="INFILE")
    parser.add_option("-o", "--outfile", dest="outfile", default="tf.html", 
                      help="Location of resulting html file", metavar="OUTFILE")
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options


def main():
    opt = ParseCmdLineOptions()
    
    print "Loading CSV file:%s"%opt.infile
    try:
        tfi = TfCsvImport( opt.infile )
        tfi.EnableImportByTeacher('Teacher 7')       
    except ValueError as e:
        print "Failed to load csv file: %s (Reason: %s)"%(opt.infile, e.message)
        exit(1)
    
    print "Processing data and generating HTML"
    TO = TableOutput( tfi )
    HTML = TO.GetHtmlTable()
    
    print "Resulting HTML"
    print HTML
    
if __name__ == '__main__': 
    main()