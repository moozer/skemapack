#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Nov 9, 2010

@author: pfl
'''

#from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPage, ProcessFile
#from Output.IcsOutput.IcsOutput import IcsOutput
import Input.HtmlGetter.loadWebPage.loadHtml as HtmlGetter
from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper

from Output.Calendar.Gmail.gmailOutput import GmailOutput_API

from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin


def main():
    myConfig = SkemaPackConfig( SkemaPackConfig_stdin() )
    
    print myConfig.get("SkemaScraper","Dateformat")
    
    myHtmlGetter = HtmlGetter.htmlGetter()
    htmlResponse = myHtmlGetter.getSkemaWithPost(myConfig.get("SkemaScraper","TeacherId"),3,5)
    response = htmlResponse.read()
    print response
    htmlScraper = SdeSkemaScraper(DateFormat = myConfig.get("SkemaScraper","Dateformat"))
    
    htmlScraper.feed(response)
    

    try:
        myGmailOutput = GmailOutput_API(myConfig.get("gmail","username"),myConfig.get("gmail","Password"))
    except :
        #TODO : GmailOutput_API should raise a common exception when gdata throws gdata.service.BasAuthentication
        print ( "login to gmail failed - please check username and password")
        exit()
    
    
    for Appointment in htmlScraper.Appointments:
        print Appointment
        myGmailOutput.addAppointment(Appointment)
    
    return 0

if __name__ == '__main__': 
    main()
