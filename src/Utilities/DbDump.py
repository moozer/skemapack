'''
Created on May 18, 2011

@author: morten
'''

# handling pythonpath
from PythonPathUtil import AppendSrcToPythonPath
AppendSrcToPythonPath()

from optparse import OptionParser
from Datatypes.ActivityDb import ActivityDb

def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile", default = None,
                      help="Location of TF database file to read", metavar="INFILE")
#    parser.add_option("-o", "--outfile", dest="outfile", default="tf.html", 
#                      help="Location of resulting html file", metavar="OUTFILE")
#    parser.add_option("--teachers", dest="teachers", default = None,
#                      help="A comma separated list of teacher initials", metavar="TEACHERS")
    parser.add_option("-c", "--class", dest="classname", default = None,
                      help="Class name ", metavar="CLASS")
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
    
    print "Loading database file: %s"%opt.infile
    ADb = ActivityDb( opt.infile, FailOnNonExist = True )

    TeacherList = {}
    CourseList = {}
    for Activity in ADb.GetActivities():
        if opt.classname:
            if Activity.getClass() == opt.classname:
                TeacherList[Activity.getTeacher()] = None
                CourseList[Activity.getCourse()] = None
        else:
            TeacherList[Activity.getTeacher()] = None
            CourseList[Activity.getCourse()] = None

    if opt.classname:
        print "Listing for class %s" % opt.classname
    else:
        print "Listing all course and teachers"
    
    print "Teachers:"
    for Teacher in TeacherList.keys():
        print Teacher
    
    print "--"
    print "Courses:"
    for Course in CourseList.keys():
        print Course
    
if __name__ == '__main__':
    main()
    pass