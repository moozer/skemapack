'''
Created on Nov 9, 2010

@author: pfl
'''

from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPage, ProcessFile
from Output.IcsOutput.IcsOutput import IcsOutput

def ParseCmdLineOptions():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-u", "--user", dest="user",
                      help="Gmail user name", metavar="USER")
    parser.add_option("-p", "--passwd", dest="pw",
                      help="Gmail password", metavar="PW")
    parser.add_option("-u", "--url", dest="url", default="http://skema.sde.dk/laerer/5421/en-US.aspx",
                      help="Skema url", metavar="URL")
    
    (options, args) =  parser.parse_args()
    
    #~ if options.infile and options.url:
        #~ parser.error( "-i and -u are mutually exclusive" )  
    
    return options


def main():
    opt = ParseCmdLineOptions()
    
#===============================================================================
#    if opt.infile:
#        Apps = ProcessFile( opt.infile )
#    else:
#        Apps = ProcessWebPage( opt.url)
#    print len(Apps), "appointments extracted"
#    
#    #print Apps[0]['Subject']
#    io = IcsOutput( Apps )
# 
#    FileName = "SkemaCurrentWeek.ics"
#    f = open( FileName, "wb" )
#    f.write( io.GetIcsString() )
#    f.close()
#    print "Ics file saved as", FileName
#===============================================================================
    
    return 0

if __name__ == '__main__': main()
