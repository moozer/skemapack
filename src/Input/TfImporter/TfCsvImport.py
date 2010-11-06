
'''
Created on Nov 6, 2010

@author: morten
'''

class TfCsvImport():
    '''
    Import TF data from csv file 
    '''

    def __init__( self, CsvInputFilename):
        '''
        @param CsvInputFilename The file to retrieve data from.
        '''
        self._InputFile = CsvInputFilename
        
# --- get/set functions --
    def getCsvFilename( self ):
        ''' returns the csv file specified for input '''
        return self._InputFile
    
# --- other methods ---
    def EnableImportByTeacher( self, TeacherInitials ):
        '''
        Searches the file for lecture based on a specific teacher
        '''
        