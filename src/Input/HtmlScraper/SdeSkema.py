'''
Created on Sep 7, 2011

@author: morten
'''

from SdeSkemaScraper import SdeSkemaScraper

def SdeSkema( data, DateFormat = "%m/%d/%Y", TimeFormat = "%H:%M"):
    ''' Iterator the wraps the class. For convenience.
    '''
    scraper = SdeSkemaScraper( DateFormat, TimeFormat )
    scraper.feed(data)
    
    for App in scraper.Appointments:
        yield App

    scraper.close()