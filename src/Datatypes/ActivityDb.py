'''
Created on May 6, 2011

@author: morten
'''

import sqlite3, os

class ActivityDb():
    '''
    classdocs
    '''

    def __init__(self, DbFile):
        '''
        Constructor
        @param DbFile The file to use. Try ':memory:'
        '''
        self._DbFile = DbFile
        self._conn = sqlite3.connect(DbFile)

        self._BaseDbFile = "Datatypes/BaseDb.sql" # sql file used for initialization of db
        self._InitDb(self._BaseDbFile)

                
    def getMetadata(self):
        c = self._conn.cursor()
        c.execute('select key, value from metadata')
        
        retval = {}
        for row in c:
            retval[row[0]] = row[1]

        return retval
        
    def _InitDb( self, Filename ):
        c = self._conn.cursor()

        # Create table
        f = open( Filename )
        sqldata = f.read()
        f.close()
        c.executescript(sqldata)
        
        # Save (commit) the changes and close cursor
        self._conn.commit()
        c.close()
   