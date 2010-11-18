#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Nov 9, 2010

@author: pfl
'''

#from Input.HtmlScraper.BeautifulSkemaScraper import ProcessWebPage, ProcessFile

from Output.TableOutput.TableOutput import TableOutput
from Input.TfImporter.TfCsvImport import TfCsvImport

def main():
    
#    myImporter = TfCsvImport('/home/pfl/sandbox/python/TF_extractor/tf.csv')
#    myImporter.EnableImportByTeacher('PFL')
#    
#    for entry in myImporter.GetNextEntryIterator():
#        print entry
     
     
     
    myImporter = TfCsvImport('/home/pfl/sandbox/python/TF_extractor/tf.csv')
    myImporter.EnableImportByTeacher('PFL')
    
    myTable = TableOutput(myImporter.GetNextEntryIterator())

    #print myTable.GetTextileTable(1, 26)
    print (myTable.GetHtmlTable(1,26))
    
    
    return 0

if __name__ == '__main__': main()
