'''
Created on Mar 29, 2012

@author: flindt
'''
import os



def DumpNamedSheet(XmlFileName, CsvFileName, SheetName, Seperator):
    
    
    Cmd = "libreoffice"
    Cmd = '%s %s --headless --norestore "--accept=socket,host=localhost,port=2002;urp;"'%(Cmd, "\"%s\""%XmlFileName)
       
    print "issuing: %s"%Cmd
    os.system( Cmd )
    
    pass


