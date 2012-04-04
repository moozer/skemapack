'''
Created on Mar 29, 2012

@author: flindt
'''
import os,time
import getopt,sys
#import socket  # only needed on win32-OOo3.0.0
import uno
import unohelper

from com.sun.star.beans import PropertyValue


def DumpNamedSheet(XmlFileName, CsvFileName, SheetName, Separator):
    
    
    Cmd = "libreoffice"
    Cmd = '%s %s --headless --norestore "--accept=socket,host=localhost,port=2002;urp;"'%(Cmd, "\"%s\""%XmlFileName)
       
    print "issuing: %s"%Cmd
    # os.system( Cmd ) wont work, since it wait for the process to end...
    #os.popen(Cmd)
    time.sleep(0.5)
    
    # get the uno component context from the PyUNO runtime
    localContext = uno.getComponentContext()
    
    # create the UnoUrlResolver
    resolver = localContext.ServiceManager.createInstanceWithContext(
                    "com.sun.star.bridge.UnoUrlResolver", localContext )
    
    # connect to the running office
    ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
    smgr = ctx.ServiceManager
    
    # get the central desktop object
    desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)
    
    # access the current calc document
    model = desktop.getCurrentComponent()
    
    
    sheet = model.Sheets.getByName(SheetName)
    
    
    # Now save it in CSV format.
    filename = CsvFileName
    os.path.expanduser(filename)
    filename = os.path.abspath(filename)
    out_props = (
            PropertyValue("FilterName", 0, "Text - txt - csv (StarCalc)", 0),
            PropertyValue("Overwrite", 0, True, 0),
            PropertyValue("Separator", 0, Separator, 0),
            )
    csv_url = unohelper.systemPathToFileUrl(filename)
    model.storeToURL( csv_url, out_props)
    
    time.sleep(1)
    model.dispose()

    
    
    pass


