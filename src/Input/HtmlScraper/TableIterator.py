'''
Created on Nov 14, 2010

@author: morten
'''
import BeautifulSoup

def TableIterator( Html ):
    ''' generator to loop over the rows in a html  
    Uses beautiful soup to extract the data, starts by locating the table
    @param TableHtml: The html data to parse
    @return Use "for row in TableIterator(htmltable): blabla"
    '''
    
    soup = BeautifulSoup.BeautifulSoup( Html )
    for Table in soup.findAll( 'table' ):
        allrows = Table.findAll('tr')
        for row in allrows:
            RowArray = []
            allcols = row.findAll('td')
            for col in allcols:
                thestrings = [unicode(s) for s in col.findAll(text=True)]
                thetext = ''.join(thestrings)
                RowArray.append(thetext)
            yield RowArray
    raise StopIteration
