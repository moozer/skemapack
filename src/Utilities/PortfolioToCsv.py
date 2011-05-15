'''
Created on May 15, 2011

@author: morten
'''

from optparse import OptionParser
from Input.FronterPortfolio.FronterPortfolio import FronterPortfolio

def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile", 
                      help="File to read html data from", metavar="INFILE")
    parser.add_option("-o", "--outfile", dest="outfile", default="portfolio.csv",
                      help="Filename of output file", metavar="OUTFILE")        
    
    (options, args) =  parser.parse_args()

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
        print "%d Student %s" % StudentList[i]
        outfile.write( StudentList[i])
        for HandinName in sorted( StudentHandins.iterkeys() ):
            outfile.write( "\t%s"% StudentHandins[HandinName])
        outfile.write( "\n")
        i = i + 1
        
    print "done"
        