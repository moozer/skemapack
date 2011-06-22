'''
Created on May 28, 2011

@author: morten
'''

from PythonPathUtil import AppendSrcToPythonPath #@UnusedImport
from optparse import OptionParser
from Datatypes.ActivityDb import ActivityDb
from Output.TableOutput.HtmlOutput import HtmlOutput

Header = '''<html>
    <header>
        <title>TF</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style TYPE="text/css"> 
        <!-- 
            table { border: solid 1px black;
                    text-align: center } 
            tr    { background: #ddd; }
            .NotEqual { width: 100%; }
            .NotEqual tr { background: #b33; }
            .Equal    { width: 100%; }
        --> 
        </style>
    </header>
    <body>
    '''
Footer = '''    </body>
</html>'''
    


def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile",
                      help="Database file to use", metavar="INFILE")
    parser.add_option("-c", "--comparefile", dest="cmpfile", default = None,
                      help="Database file to use in comparison" )
    parser.add_option("-o", "--outfilebase", dest="outfilebase", default="TF_", 
                      help="Basename of files", metavar="OUTFILEBASE")
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



def WriteTeacherTable(CurTeacher, HtmlToOutput, filehandle):
    ''' writes the table to file '''
    filehandle.write("<h2>Course for teacher %s</h2>" % CurTeacher)
    filehandle.write(HtmlToOutput)
    filehandle.write("<br />")


def WriteHeader(filehandle):
    filehandle.write(Header)

def WriteFooter(filehandle):
    filehandle.write(Footer)


def main():
    opt = ParseCmdLineOptions()
    
    f = open("%sAll.html" % (opt.outfilebase,), "w")
    f.write( Header )
   
    print "Loading database file: %s"%opt.infile
    ADb = ActivityDb( opt.infile )

    AllTeachers = ADb.GetTeacherList().keys()
    
    f.write( "<h2>All activities</h2><br />" )
    
    print "Processing data and generating HTML"
    if not opt.cmpfile:
        print "Dataset is %s"% ADb.GetTitle()
        f.write( "Dataset is %s" % ADb.GetTitle())
        
        for CurTeacher in AllTeachers:
            HO = HtmlOutput( ADb.GetActivities( Teachers = [CurTeacher] ) )
            HTML = HO.GetHtmlTable(1, 52)
            print "Saving data to HTML (Teacher %s)" % CurTeacher
            WriteTeacherTable(CurTeacher, HTML, f)
               
            # output specific files for each teacher also         
            f_teacher = open("%s%s.html" % (opt.outfilebase, CurTeacher), "w")
            WriteHeader(f_teacher)
            f_teacher.write( "Dataset is %s" % ADb.GetTitle())
            WriteTeacherTable(CurTeacher, HTML, f_teacher)
            WriteFooter(f_teacher)
            f_teacher.close()
            print "html saved in %s"%f_teacher.name

    else:
        ADbCmp = ActivityDb( opt.cmpfile )
        f.write( "First dataset is %s <br />" % ADb.GetTitle())
        f.write( "Second dataset is %s <br />" % ADbCmp.GetTitle())
        print "First dataset is %s" % ADb.GetTitle()
        print "Second dataset is %s" % ADbCmp.GetTitle()
        
        for CurTeacher in AllTeachers:
            HO = HtmlOutput( ADb.GetActivities( Teachers = [CurTeacher], SortBy = 'class,name'), 
                             ADbCmp.GetActivities( Teachers =  [CurTeacher], SortBy = 'class,name ' ) )
            HTML = HO.GetHtmlTable(1, 52)        
            print "Saving data to HTML (Teacher %s)" % CurTeacher
            f.write( "<h2>Course for teacher %s</h2>" % CurTeacher )
            f.write( HTML )
            f.write( "<br />")

    f.write( Footer )
    print "html saved in %s"%f.name
    
    
if __name__ == '__main__':
    main()