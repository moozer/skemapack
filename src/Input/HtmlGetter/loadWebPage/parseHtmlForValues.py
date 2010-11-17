'''
Created on Oct 13, 2010

@author: pfl
'''
  
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.values = {}
    
    def handle_starttag(self, tag, attrs):
        self._name = ''
        self._value = ''
        if tag == "input":
            for attr in attrs:
                if attr[0] == 'name':
                    self._name = attr[1]
                if attr[0] == 'value':
                    self._value = attr[1]
            if self._name in ('__VIEWSTATE', '__EVENTVALIDATION', u'ctl00$ContentPlaceHolder1$Localizedbutton3'):#if self._name in ('__VIEWSTATE', '__EVENTVALIDATION'):
                self.values[ self._name ] = self._value

