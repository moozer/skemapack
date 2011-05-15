'''
Created on May 15, 2011

@author: morten
'''
from BeautifulSoup import BeautifulSoup


class FronterPortfolio(object):
    '''
    classdocs
    '''


    def __init__(self, HtmlFilename):
        '''
        Constructor
        '''
        self._Filename = HtmlFilename
        file = open( HtmlFilename, "r" )
        self._html = file.read()
        file.close()
        
    def getFilename(self):
        return self._Filename
        
    def getStudentNames(self):
        StudentNames = []
        soup = BeautifulSoup(self._html)
        entries = soup.findAll('tr', {'class':"tronhover"})
        for entry in entries:
            tds = entry.findAll('span')
            for td in tds:
                if td != None:
                    StudentNames.append( td['title'] )
        
        return StudentNames

    def getHandins(self):
        Handins = []
        soup = BeautifulSoup(self._html)
        maindivs = soup.findAll( 'div', {'id': 'enclosure_div'})
        for maindiv in maindivs:
            entries = maindiv.findAll('th', {'class':"label2"})
            for entry in entries:
                tds = entry.findAll('a')
                for td in tds:
                    if td != None:
                        Handins.append( td['title'] )
        
        return Handins


