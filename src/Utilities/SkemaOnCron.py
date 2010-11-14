#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Nov 14, 2010

@author: morten
'''

# includes
from optparse import OptionParser
import datetime, os, filecmp, shutil
from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPageById
from Output.IcsOutput.IcsOutput import IcsOutput

def ParseCmdLineOptions():
    """Parses the command line options and  sets defaults 
    @return: A dictionary containing the parameters
    """
    parser = OptionParser()
    parser.add_option("-I", "--id", dest="id", type="int", default = 5421,
                      help="Id of teacher or room", metavar="ID")    
    parser.add_option("-n", "--num-weeks", dest="nweeks", type="int", default = 5,
                      help="The number of weeks to fetch", metavar="NWEEK")    
    parser.add_option("-d", "--work-dir", dest="workdir",
                      help="The directory used for data", metavar="WORKDIR")    

    (options, args) =  parser.parse_args()
    return options

if __name__ == '__main__':
    # constants
    TempOutputFilename = "TempIcsOutput.ics"
    IcsDataFilename = "FromCron.ics"
    DiffFilename = "Diff.txt"
    DefaultDateformat = "%d-%m-%Y"
    
    opt = ParseCmdLineOptions()
    
    CurrentWeek = datetime.datetime.now().isocalendar()[1]

    # parameter check
    if not opt.id:
        print "Please supply an Id (using --id)"
        exit(1)
        
    if opt.workdir:
        os.chdir(opt.workdir)
        
    print "Fetching data from week %i and the following %i weeks."%(CurrentWeek, opt.nweeks-1)
    print "Id to fetch %i"%opt.id
    
    # get data and create .ics file
    try:
        Apps = ProcessWebPageById( Id = opt.id, DateFormat = DefaultDateformat,
                                   FirstWeek = CurrentWeek, LastWeek = CurrentWeek+opt.nweeks-1 )
    except ValueError as e:
        print "Error processing data from web. (ValueError: %s)"%e.message
        print "Check dateformat. Current is %s"%DefaultDateformat
        exit(2)
    except Exception as e:
        print "Unknown exception while collecting appointments: %s" % type(e)
        exit(3)
    print "%i appointments extracted"%len(Apps)
    io = IcsOutput( Apps )

    # saving temp ics file    
    f = open( TempOutputFilename, "wb" )
    f.write( io.GetIcsString() )
    f.close()

    # doing comparison
    print "Comparing %s and %s"%(TempOutputFilename, IcsDataFilename)
    try:
        CmpRes = filecmp.cmp( TempOutputFilename, IcsDataFilename )
    except OSError as e:
        print "Comparison failed or other system call failed - assuming missing or corrupt current data file."
        CmpRes = False

    if CmpRes:
        print "Files match. No change."
    else:
        print "Files differ - using newest"
        print "Saving latest data in %s"%IcsDataFilename
        
        print "Diff dump follows"
        os.system( "diff %s %s"%( TempOutputFilename, IcsDataFilename ))

        shutil.copy2( TempOutputFilename, IcsDataFilename )                        

        