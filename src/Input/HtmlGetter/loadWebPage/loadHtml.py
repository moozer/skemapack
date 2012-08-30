'''
Created on Oct 12, 2010

@author: pfl
'''
import urllib, httplib, datetime

from parseHtmlForValues import MyHTMLParser as ParseForValues
 

class htmlGetter(object):
    '''
    loads the skema web page for a particular person /  class / room
    parses it to get the keys needed to do a POST and get skema for more than one week
    does a POST to get the full skema for the period wanted
    '''


    def __init__(self, site = "skema.sde.dk"):
        ''' Initialisation
        '''
        self._site = site
    
    def getSkemaWithPost(self, idx, weekStart=1, weekEnd=52, year=0):
        ''' Does a POST to get the skema for the person/room indicated by idx 
        
        @param idx: The id of the teacher or room to extract schedule for, e.g. 3735 for PFL
        @param weekStart: The first week of the schedule to fetch
        @param weekEnd: The last week of the schedule to fetch
        @param year: The year. Defaults to current year
        @return: A connection to the page showing the desired weeks.      
        '''
        # TODO: Support for different starting and ending year (perhaps just if startWeek > EndWeek?)
        # TODO: Check if dates can be used and not week numbers
        
        # stuff to force type checking in params
        idx = int( idx)
        weekStart = int( weekStart )
        weekEnd = int( weekEnd )
        year = int( year )
        
        # handle default year
        if year == 0:
            year = datetime.datetime.now().year
        
        self._params = { 'id': idx, 'startWeek': weekStart, 'endWeek': weekEnd, 'year': year}
        
        self._getInitialPage(idx)
        self._parseForValues(weekStart, weekEnd, year)
        self._doPost(idx)
        return self._postResult
        
    def getParameters(self):
        ''' Sanity check function
        @returns A collection of the parameters used in extraction
        ''' 
        return self._params
        
    def _getInitialPage(self, idx ):
        URL = 'http://%s/laererSkema.aspx?idx=%i&lang=da-DK'%(self._site, idx)
        self._initialPage = urllib.urlopen( URL ).read()
        if self._initialPage.find( 'IndexOutOfRange' ) <> -1:
            raise IndexError   
        
    def _parseForValues(self, weekStart, weekEnd, year):
        parser = ParseForValues()
        parser.feed(self._initialPage)  
        params = urllib.urlencode(parser.values)
        params += '&' + urllib.urlencode({ 'ctl00$ContentPlaceHolder1$weeknrstart' : str(weekStart),'ctl00$ContentPlaceHolder1$weeknrend': str(weekEnd), \
                                          'ctl00$ContentPlaceHolder1$weekyear' : str( year ), \
                                          'ctl00$ContentPlaceHolder1$Localizedbutton1' : 'Hent+valgte+ugers+skema', \
                                          'ctl00$ContentPlaceHolder1$myweekstart' : '2012-01-23', \
                                          'ctl00$ContentPlaceHolder1$myweekend' : '2012-01-28'})
        self._values = params
        # The two dates in the request seems to be ignored, so they are left hardcoded for now
        
    def _doPost(self, idx ):
        ''' Use the values from the Initial page to do a post and get the whole skema '''
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPConnection('skema.sde.dk:80')
        conn.request("POST", "/laererSkema.aspx?idx=%i&amp;lang=da-DK"%idx, self._values, headers)
        self._postResult = conn.getresponse()
        
    
# TODO: move this to a test  
if __name__ == "__main__":
    myget = htmlGetter()
    print myget.getSkemaWithPost(3735,4,5,2012).read()
    