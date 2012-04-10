#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 10 Feb 2012

@author: moz
'''

import sys
from Configuration.SkemaPackConfig import SkemaPackConfig
from Import.ImportFile import ImportFile
from Output.HtmlTableOutput import HtmlTableOutput

Header = '''<html>
    <header>
        <title>TF</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style TYPE="text/css"> 
        <!-- 
            table { border: solid 1px black; } 
            tr    { background: #ddd }
            td.WeekHeader { -webkit-transform: rotate(270deg);
                            -moz-transform: rotate(270deg);
                            -o-transform: rotate(270deg);
                            writing-mode: lr-tb; }
        --> 
        </style>
    </header>
    <body>
    '''
Footer = '''    </body>
</html>'''
    

def ExportHtml( Weeksums, config, ConfigSet = "ExportHtml"):
    # open output file.
    Outfile = config.get( ConfigSet, 'OutFile' )
    
    f = open(Outfile, "w")
    f.write( Header )

    # get flags
    Headers = config.get( ConfigSet, 'GroupBy' )
    IncludeRowSums = config.getboolean( ConfigSet, 'RowSums' ) 
    IncludeColumnSums = config.getboolean( ConfigSet, 'ColumnSums' )
    
    HeadersList = filter(lambda x: x.strip(), Headers.split(','))
    
    # output all - filter elsewhere
    Html = HtmlTableOutput( Weeksums, 
                            RowSums = IncludeRowSums, ColSums = IncludeColumnSums,
                            Headers =  HeadersList )

    # save to html
    f.write( "<h2>Schedule showing all entries</h2><br />")
    f.write( Html )
    f.write( "<br />")        
    
    # and close
    f.write( Footer )
    return

if __name__ == '__main__':
    # allow cfg file from cmd line
    if len(sys.argv) > 1:
        cfgfile = open( sys.argv[1] )
        config = SkemaPackConfig( cfgfile )
        sys.stderr.write( "ExportHtml : config file is %s\n"%cfgfile.name)
    else:
        config = None
        sys.stderr.write( "ExportHtml : config file is %s\n"%"<stdin>")


#    # 1) read config/parameter
    ConfigSet = "ExportHtml"

    # 3) import from file (which might be stdin
    Events, config = ImportFile( config, ConfigSet )
    print config
    # 4) output all events to ics
    ExportHtml( Events, config )


