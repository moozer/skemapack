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
                    if td['title'].find("(") == -1: # eliminate entries containing "(Slettes om nn dage)"
                        StudentNames.append( {'Name': td['title'], 'Include': True} )
                    else:
                        StudentNames.append( {'Name': td['title'], 'Include': False} )
        
        return StudentNames

    def getHandinTitle(self):
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

    def getHandinsByStudent(self):
        ''' currently all students '''
        soup = BeautifulSoup(self._html)
        maindivs = soup.findAll( 'div', {'id': 'enclosure_div'})
        
        HandinTitles = self.getHandinTitle()
        
        for maindiv in maindivs:
            entries = maindiv.findAll('tr', {'class':"tronhover"})
            for entry in entries:
                tds = entry.findAll('td')
                Handins = []

                for td in tds:
                    try:
                        Handins.append( td.a.img['title'] )
                    except:
                        Handins.append(  "<none>" )
            
                # making return dictionary    
                if len(Handins) != len(HandinTitles):
                    raise ValueError("Data error, title and data size mismatch")

                ret = {}
                for i in range( 0, len(Handins )):
                    if Handins[i] in ['Not approved', 'Not delivered']:
                        Missing = True
                    else: # i.e. in progress, approved, not eval
                        Missing = False
                        
                    if Handins[i] in ['In progress', 'Not evaluated']:
                        Pending = True
                    else:   # ie. not approved, not devlivere, approved
                        Pending = False
                    
                    
                    ret[HandinTitles[i]] = {'Evaluation': Handins[i], 
                                            'Course': HandinTitles[i].split(' ')[0], 
                                            'Missing': Missing, 'Pending': Pending }
                yield ret

        raise StopIteration

        
