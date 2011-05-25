#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2010

@author: morten
'''

from optparse import OptionParser
from Input.TfImporter.TfCsvImport import TfCsvImport
from Input.TfImporter.TfExtraCsvImport import TfExtraCsvImport
from Output.TableOutput.TableOutput import TableOutput

Header = '''<html>
    <header>
        <title>TF</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style TYPE="text/css"> 
        <!-- 
            table { border: solid 1px black; } 
            tr    { background: #ddd }
        --> 
        </style>
    </header>
    <body>
    '''
Footer = '''    </body>
</html>'''
    


def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile", default = None,
                      help="Location of TF csv file to read", metavar="INFILE")
    parser.add_option("-o", "--outfile", dest="outfile", default="tf.html", 
                      help="Location of resulting html file", metavar="OUTFILE")
    parser.add_option("--teachers", dest="teachers", default = None,
                      help="A comma separated list of teacher initials", metavar="TEACHERS")
    parser.add_option("--classes", dest="classes", default = None,
                      help="A comma separated list of class name", metavar="CLASSES")
    parser.add_option("-x", "--extrafile", dest="extrafile", default = None,
                      help="Extra csv data to include", metavar="EXTRAFILE")
    parser.add_option("-s", "--startweek", dest="startweek", type="int", default = 1,
                      help="The start week number (default: 1)", metavar="STARTWEEK")
    parser.add_option("-e", "--endweek", dest="endweek", type="int", default = 52,
                      help="The end week number (default: 52)", metavar="ENDWEEK")
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options


def main():
    opt = ParseCmdLineOptions()
    
    # Checking params
    if not opt.teachers and not opt.classes:
        print "No teacher or classes to search for. Please supply a list using --teachers or --classes"
        exit(2)

    f = open(opt.outfile, "w")
    f.write( Header )
    
    print "Loading CSV file:%s"%opt.infile
    tfi = TfCsvImport( opt.infile )
    if opt.extrafile:
        tfix = TfExtraCsvImport( opt.extrafile )
    else:
        tfix = None
        
    try:
        if opt.teachers:
            for Teacher in opt.teachers.split(','):
                tfi.EnableImportByTeacher(Teacher)
                if tfix is not None:
                    tfix.EnableImportByTeacher(Teacher)
                
                print "Processing data and generating HTML for teacher %s"%Teacher
                TO = TableOutput( tfi, ItObjectExtra=tfix,
                                  IncludeHeader=True, IncludeRowSums=True, 
                                  IncludeColumnSums=True, IncludePreperation=True )
                HTML = TO.GetHtmlTable(opt.startweek, opt.endweek)
                
                print "Saving HTML"
                f.write( "<h2>Schedule for %s</h2><br />"%Teacher)
                f.write( HTML )
                f.write( "<br />")

        if opt.classes:                
            for Class in opt.classes.split(','):
                tfi.EnableImportByClass(Class)
                if tfix is not None:
                    tfix.EnableImportByClass(Class)
                
                print "Processing data and generating HTML for Class %s"%Class
                TO = TableOutput( tfi, IncludeHeader=True, IncludeRowSums=True, IncludeColumnSums=True )
                HTML = TO.GetHtmlTable(opt.startweek, opt.endweek)
                
                print "Saving HTML"
                f.write( "<h2>Schedule for %s</h2><br />"%Class)
                f.write( HTML )
                f.write( "<br />")
    except ValueError as e:
        print "Failed to load or process csv file (Reason: %s)"%(opt.infile, e.message)
        exit(1)

    f.write( Footer )
    print "html saved in %s"%opt.outfile
    
if __name__ == '__main__': 
    main()