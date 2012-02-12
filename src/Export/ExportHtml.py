'''
Created on 10 Feb 2012

@author: moz
'''

import sys
from Configuration.SkemaPackConfig import SkemaPackConfig, SkemaPackConfig_stdin_eal
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
    sys.stderr.write( "ExportHtml : output file is %s\n"%Outfile )

    f = open(Outfile, "w")
    f.write( Header )

    # get flags
    # TODO: add flag support to 
#    IncludeHeader = config.get( ConfigSet, 'HeaderSums' )
#    IncludeRowSums = config.get( ConfigSet, 'RowSums' ) 
#    IncludeColumnSums = config.get( ConfigSet, 'ColumnSums' )
    
    # output all - filter elsewhere
    sys.stderr.write(  "Processing data and writing HTML using all entries\n" )
    
    Html = HtmlTableOutput( Weeksums )

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
    else:
        cfgfile = SkemaPackConfig_stdin_eal()

    sys.stderr.write( "ExportHtml : config file is %s\n"%cfgfile.name)

#    # 1) read config/parameter
    config = SkemaPackConfig( cfgfile )
    ConfigSet = "ExportHtml"

    # 3) import from file (which might be stdin
    Events = ImportFile( config, ConfigSet )
    
    # 4) output all events to ics
    ExportHtml( Events, config )


