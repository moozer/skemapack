'''
Created on Nov 14, 2010

@author: morten
'''
import BeautifulSoup

def TableIterator( TableHtml ):
    ''' generator to loop over the rows in a html table 
    Uses beautiful soup to extract the data.
    @param TableHtml: The html data to parse
    @return Use "for row in TableIterator(htmltable): blabla"
    '''

    soup = BeautifulSoup.BeautifulSoup(TableHtml)
    allrows = soup.findAll('tr')
    for row in allrows:
        RowArray = []
        allcols = row.findAll('td')
        for col in allcols:
            thestrings = [unicode(s) for s in col.findAll(text=True)]
            thetext = ''.join(thestrings)
            RowArray.append(thetext)
        yield RowArray
    raise StopIteration
