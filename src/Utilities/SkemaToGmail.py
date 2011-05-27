# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Nov 9, 2010

@author: pfl
'''

#from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPage, ProcessFile
from Output.IcsOutput.IcsOutput import IcsOutput
import Input.HtmlGetter.loadWebPage.loadHtml as HtmlGetter
from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper

from Output.Calendar.Gmail.gmailOutput import GmailOutput_cli,GmailOutput_API

def ParseCmdLineOptions():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-n", "--user", dest="user",
                      help="Gmail user name", metavar="USER")
    parser.add_option("-p", "--passwd", dest="pw",
                      help="Gmail password", metavar="PW")
    parser.add_option("-u", "--url", dest="url", default="http://skema.sde.dk/laerer/3735/en-US.aspx",
                      help="Skema url", metavar="URL")
    
    parser.add_option( "-i", "--interface", dest="interface", default="cli",
                      help="Interface cli or api", metavar="CLI")
    
    (options, args) =  parser.parse_args() #@UnusedVariable
    return options


def main():
    opt = ParseCmdLineOptions()
    
    print (opt.user)
    print (opt.pw)
    print (opt.url)
    print (opt.interface)
    
    myHtmlGetter = HtmlGetter.htmlGetter()
    htmlResponse = myHtmlGetter.getSkemaWithPost(3735,43,52)
    
    htmlScraper = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
    htmlScraper.feed(htmlResponse.read())
    
    if opt.interface == "cli":
        myGmailOutput = GmailOutput_cli("poul.flindt.skema","minmine1")
    else:
        try:
            myGmailOutput = GmailOutput_API("poul.flindt.skema","minmine1")
        except :
            #TODO : GmailOutput_API should raise a common exception when gdata throws gdata.service.BasAuthentication
            print ( "login to gmail failed - please check username and password")
            exit()
    
    
    for Appointment in htmlScraper.Appointments:
        myGmailOutput.addAppointment(Appointment)
    
    
    
    return 0

if __name__ == '__main__': main()
