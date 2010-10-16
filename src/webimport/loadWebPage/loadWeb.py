'''
Created on Oct 12, 2010

@author: pfl
'''
import urllib

from parseHtmlForValues import MyHTMLParser as ParseForValues
 

class loadWebClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def _printWebPage(self):
        '''
        
        Load a page and print the content to stdout
        '''
        page1 = urllib.urlopen('http://skema.sde.dk/laererSkema.aspx?idx=3735&lang=da-DK').read() 
        parser1 = ParseForValues()
        parser1.feed(page1)  
        print parser1.values   
        params = urllib.urlencode(parser1.values)
        params += '&' + urllib.urlencode({'ctl00$ContentPlaceHolder1$weeknrend' : '52','ctl00$ContentPlaceHolder1$weeknrstart' : '1', 'ctl00$ContentPlaceHolder1$weekyear' : '2010'})
        print params
        
        
        