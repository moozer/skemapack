'''
Created on May 8, 2011

@author: morten
'''
from PythonPathUtil import AppendSrcToPythonPath #@UnusedImport
from optparse import OptionParser
from Datatypes.ActivityDb import ActivityDb
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
                      help="Database file to use", metavar="INFILE")
    parser.add_option("-o", "--outfile", dest="outfile", default="tf.html", 
                      help="Location of resulting html file", metavar="OUTFILE")
#    parser.add_option("--teachers", dest="teachers", default = None,
#                      help="A comma separated list of teacher initials", metavar="TEACHERS")
#    parser.add_option("--classes", dest="classes", default = None,
#                      help="A comma separated list of class name", metavar="CLASSES")
#    parser.add_option("-x", "--extrafile", dest="extrafile", default = None,
#                      help="Extra csv data to include", metavar="EXTRAFILE")
#    parser.add_option("-s", "--startweek", dest="startweek", type="int", default = 1,
#                      help="The start week number (default: 1)", metavar="STARTWEEK")
#    parser.add_option("-e", "--endweek", dest="endweek", type="int", default = 52,
#                      help="The end week number (default: 52)", metavar="ENDWEEK")
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options


def main():
    opt = ParseCmdLineOptions()
    
    f = open(opt.outfile, "w")
    f.write( Header )
    
    print "Loading database file: %s"%opt.infile
    ADb = ActivityDb( opt.infile )
            
    print "Processing data and generating HTML"
    TO = TableOutput( ADb.GetActivities(),
                      IncludeHeader=True, IncludeRowSums=True, 
                      IncludeColumnSums=True, IncludePreperation=True )
    HTML = TO.GetHtmlTable(1, 52)

    print "Saving HTML"
    f.write( "<h2>All activities</h2><br />" )
    f.write( HTML )
    f.write( "<br />")

    f.write( Footer )
    print "html saved in %s"%opt.outfile
    
if __name__ == '__main__': 
    main()