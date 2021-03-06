#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Nov 14, 2010
This utility is intended to be run as a cron job.

@author: morten
'''

# includes 
from Other.PythonPathUtil import AppendSrcToPythonPath #@UnusedImport
from optparse import OptionParser
import datetime, os, filecmp, shutil
from Input.HtmlScraper.SdeSkemaScraper import ProcessWebPageById
from Input.HtmlScraper.DalumSkemaScraper import DalumSkemaScraper
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
    parser.add_option("-P", "--parser", dest="parser", default = "SDE",
                      help="The parser to use (SDE or Dalum)", metavar="PARSER")    
    parser.add_option("-o", "--outputfile", dest="outfile", default = "FromCron.ics",
                      help="The name of the resulting .ics file", metavar="OUTFILE")
    parser.add_option("-O", "--offset", dest="offset", default = 0, type = "int",
                      help="Startweek offset in week numbers (relative to current)", metavar="OFFSET")
    parser.add_option("-E", "--email", dest="email", default = 0,
                      help="list of email to sent to, if skema has changed", metavar="EMAIL")
    parser.add_option("-f", "--force", dest="force", default = False, action="store_true",
                      help="If set to true, skema is considered changed regardless of the actual state", 
                      metavar="FORCE")
    
    (options, args) =  parser.parse_args() #@UnusedVariable
    return options

def SendFile( Recipients, Filename ):
    """ Sends the specified file as an email attachment
    Function is mostly copied from http://docs.python.org/library/email-examples.html
    
    @param Filename The file to send
    @param Recipient A comma separated list of email addresses
    """
    # Import smtplib for the actual sending function
    import smtplib
    
    # Here are the email package modules we'll need
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = 'Skemachanges'
    msg['From'] = "Skemapack autogenerated mail <noreply@nowhere.net>"
    msg['To'] = Recipients
    msg.preamble = 'This is the preamble...'
    
    # the message
    TextToSend = '''Hi
    
This is an autogenerated message. An Ics file is attached.
    
Have a nice day.
'''
    Message = MIMEText(TextToSend, "plain")
    msg.attach(Message)
    
    # handle the file
    fp = open(Filename, 'rb')
    IcsDataFile = MIMEText(fp.read(), _subtype='plain')
    fp.close()
    IcsDataFile.add_header('Content-Disposition', 'attachment', filename="Skema.ics")
    msg.attach(IcsDataFile)

    # Send the email via our own SMTP server.
    s = smtplib.SMTP( "localhost")
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

if __name__ == '__main__':
    # constants
    TempOutputFilename = "TempIcsOutput.ics"
    DefaultDateformat = "%d-%m-%Y"
    
    opt = ParseCmdLineOptions()
    
    StartWeek = datetime.datetime.now().isocalendar()[1] + opt.offset

    # parameter check
    if not opt.id:
        print "Please supply an Id (using --id)"
        exit(1)
        
    if opt.workdir:
        os.chdir(opt.workdir)
        
    print "Fetching data from week %i and the following %i weeks."%(StartWeek, opt.nweeks-1)
    print "Id to fetch %i using parser %s"%(opt.id, opt.parser)
    
    # get data and create .ics file
    try:
        if opt.parser == 'SDE':
            Apps = ProcessWebPageById( Id = opt.id, DateFormat = DefaultDateformat,
                                   FirstWeek = StartWeek, LastWeek = StartWeek+opt.nweeks-1, Year=0 )
        elif opt.parser == "Dalum":
            s = DalumSkemaScraper( opt.id, range(StartWeek, StartWeek+opt.nweeks)  )
            s.ExtractAppointments( NonFatal = True )
            Apps = s.GetAppointments()
        else:
            print "Invalid parser. Please specify 'SDE' or 'Dalum'"
            exit(4)
    except ValueError, e:
        print "Error processing data from web. (ValueError: %s)"%e.message
        print "Check dateformat. Current is %s"%DefaultDateformat
        exit(2)
    except Exception, e:
        print "Unknown exception while collecting appointments: %s" % type(e)
        print e.message
        exit(3)
    print "%i appointments extracted"%len(Apps)
    io = IcsOutput( Apps )

    # saving temp ics file    
    f = open( TempOutputFilename, "wb" )
    f.write( io.GetIcsString() )
    f.close()

    # doing comparison
    print "Comparing %s and %s"%(TempOutputFilename, opt.outfile)
    try:
        CmpRes = filecmp.cmp( TempOutputFilename, opt.outfile )
    except OSError, e:
        print "Comparison failed or other system call failed - assuming missing or corrupt current data file."
        CmpRes = False

    if opt.force:
        print "Force option enabled."

    if CmpRes and (not opt.force):
        print "Files match. No change."
    else:
        print "Files differ - using newest"
        print "Saving latest data in %s"%opt.outfile
        
        print "Diff dump follows"
        os.system( "diff %s %s"%( TempOutputFilename, opt.outfile ))

        shutil.copy2( TempOutputFilename, opt.outfile )                        

        if opt.email:
            SendFile( opt.email, TempOutputFilename )

