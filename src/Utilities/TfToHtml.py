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
    
    tfi = TfCsvImport( opt.infile )
    tfi.EnableImportByTeacher(u'MON')       

    TO = TableOutput( tfi )
    HTML = TO.GetHtmlTable()
    
    print HTML
    
if __name__ == '__main__': 
    main()