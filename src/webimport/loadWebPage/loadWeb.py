'''
Created on Oct 12, 2010

@author: pfl
'''
import urllib

from parseHtmlForValues import MyHTMLParser as ParseForValues
 

class loadWebClass(object):
    '''
    classdocs
    loads the skema web page for a particular person /  class / room
    parses it to get the keys needed to do a POST and get skema for more than one week
    does a POST to get the full skema for the period wanted
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def _printWebPage(self):
        '''
        This method is for development only, from this helper methods will be created
        Load a page and print the content to stdout
        '''
        page1 = urllib.urlopen('http://skema.sde.dk/laererSkema.aspx?idx=3735&lang=da-DK').read() 
        parser1 = ParseForValues()
        parser1.feed(page1)  
        print parser1.values   
        params = urllib.urlencode(parser1.values)
        params += '&' + urllib.urlencode({'ctl00$ContentPlaceHolder1$weeknrend' : '52','ctl00$ContentPlaceHolder1$weeknrstart' : '1', 'ctl00$ContentPlaceHolder1$weekyear' : '2010'})
        print params
        
        
        