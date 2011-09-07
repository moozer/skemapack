'''
Created on Sep 7, 2011

@author: morten
'''

import os

def IcsImport( IcsFileToUse ):
    '''
    @param IcsFileToUse: The file which contains the calendar entries
    '''
    f = open( IcsFileToUse, "r" )
    FileContent = f.read()
    
    yield True
    #raise StopIteration
