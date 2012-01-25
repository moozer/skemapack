#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Jan 25, 2012

@author: pfl
'''

import Input.HtmlGetter.loadWebPage.loadHtml as HtmlGetter
from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper

from Configuration.SkemaPackConfig import SkemaPackConfig,SkemaPackConfig_stdin


def main():
    myConfig = SkemaPackConfig( SkemaPackConfig_stdin() )
    
    myHtmlGetter = HtmlGetter.htmlGetter()
    htmlResponse = myHtmlGetter.getSkemaWithPost(myConfig.get("SkemaScraper","TeacherId"),\
                                                 myConfig.get("SkemaScraper","FirstWeek"),\
                                                 myConfig.get("SkemaScraper","LastWeek"))
    response = htmlResponse.read()
    
    htmlScraper = SdeSkemaScraper(DateFormat = myConfig.get("SkemaScraper","Dateformat"))
    
    htmlScraper.feed(response)
    

    for Appointment in htmlScraper.Appointments:
        print Appointment

if __name__ == '__main__': 
    main()
