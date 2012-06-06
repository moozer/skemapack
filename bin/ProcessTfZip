#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 06 Jun 2012

@author: moz
'''

from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportTfZip import ImportTfZip
from Export.ExportHtml import ExportHtml
from Filter.FilterSplit import FilterSplit
import sys, codecs

IndexHtmlText = '''
<html>
    <frameset cols="120,*">
        <frame src="%s" />
        <frame src="" name="showframe" />
    </frameset>
</html>'''

LinksHtmlText = '''
<html>
    <header>
        <title>TF links</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style TYPE="text/css"> 
        <!-- 
            table { border: solid 1px black;
                    text-align: center; } 
            tr    { background: #ddd; }
        --> 
        </style>
    </header>
    <body>
%s
    </body>
</html>
'''
IndexHtmlFilename = "index.html"
LinksHtmlFilename = "links.html"

if __name__ == '__main__':
    # Read config/parameter
    config = SkemaPackConfig( open( sys.argv[1] ) )

    # Import from skema
    print "Importing data from zip"
    events, config = ImportTfZip( config )
    print "%d entries extracted"%(len(events)+1,)

    # building list of teachers and classes in dataset
    TeacherList = {}
    ClassList = {}
    for e in events:
        if e['Teacher'] in TeacherList.keys():
            TeacherList[e['Teacher']] += 1
        else:
            TeacherList[e['Teacher']] = 0

#        if e['Class'] in ClassList.keys():
#            ClassList[e['Class']] += 1
#        else:
#            ClassList[e['Class']] = 0

    print "Extracted list of teachers and classes"
    for Teacher in TeacherList.keys():
        print "\t%s: %d entries "%(Teacher, TeacherList[Teacher])
    for Class in ClassList.keys():
        print "\t%s: %d entries "%(Class, ClassList[Class])

    
    ExportHtmlSection = "ExportHtml"
    FilterSplitSection = "FilterSplit"
    HtmlFilenameList = {}
    for Teacher in TeacherList.keys():
        print "Export to hmtl: %s "%Teacher
        config.set( ExportHtmlSection, "ClassName", "" )
        config.set( "DEFAULT", "TeacherIni", Teacher )
        FilteredEvents, config = FilterSplit( events, config )
        ExportHtml( FilteredEvents, config, ConfigSet = ExportHtmlSection )
        HtmlFilenameList[Teacher] = config.get( ExportHtmlSection, "Outfile")
    
#    for ClassName in ClassList.keys():
#        print "Export to hmtl: %s "%ClassName
#        config.set( ExportHtmlSection, "ClassName", ClassName )
#        config.set( FilterSplitSection, "ClassName", ClassName )
#        config.set( "DEFAULT", "TeacherIni", "" )
#        FilteredEvents, config = FilterSplit( events, config )
#        ExportHtml( FilteredEvents, config, ConfigSet = ExportHtmlSection )
#        HtmlFilenameList[ClassName] = config.get( ExportHtmlSection, "Outfile")
    
    # create index file
    print "Output index file: %s"%IndexHtmlFilename
    f = codecs.open(IndexHtmlFilename, 'w', 'utf-8')
    f.write(IndexHtmlText%LinksHtmlFilename )
    f.close( )
    
    print "Output index file: %s"%LinksHtmlFilename
    Links = ""
    for filedesc in HtmlFilenameList.keys():
        Links += "<a href=\"%s\" target =\"showframe\">%s</a><br/>\n"%(HtmlFilenameList[filedesc], filedesc)
        
    f = codecs.open(LinksHtmlFilename, 'w', 'utf-8')
    f.write( LinksHtmlText%Links )
    f.close()
    
    
    pass