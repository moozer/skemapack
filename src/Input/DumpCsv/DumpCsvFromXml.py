'''
Created on Mar 29, 2012

@author: flindt


Starting, stopping, etc.
  http://www.linuxjournal.com/content/starting-stopping-and-connecting-openoffice-python
  http://www.linuxjournal.com/content/convert-spreadsheets-csv-files-python-and-pyuno

'''
import os,time
import getopt,sys
#import socket  # only needed on win32-OOo3.0.0
import uno
import unohelper

from com.sun.star.beans import PropertyValue
from Input.DumpCsv.ssconverter import SSConverter



def LaunchCalcWithFile(XmlFileName):
    ''' Launches libreoofice with specified file
    Only works with files detected to be opened by calc (?)
    Breaks badly if libreoofice is running on port 2002 already
    @return: (model, desktop) - Model object (must be model.dispose()'d after use, and use desktop.terminate()
    '''
        
    Cmd = "libreoffice"
    Cmd = '%s %s --headless --norestore "--accept=socket,host=localhost,port=2002;urp;"' % (Cmd, "\"%s\"" % XmlFileName)

    print "issuing: %s" % Cmd
    # os.system( Cmd ) wont work, since it wait for the process to end...
    os.popen(Cmd)
    time.sleep(0.5)
    
    # get the uno component context from the PyUNO runtime
    localContext = uno.getComponentContext()

    # create the UnoUrlResolver
    resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)

    # connect to the running office
    ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    smgr = ctx.ServiceManager

    # get the central desktop object
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

    # access the current calc document
    model = desktop.getCurrentComponent()
    
    return model, desktop

def ShutdownCalc( desktop ):
    desktop.terminate()

def DumpNamedSheet(XmlFileName, CsvFileName, SheetName, Separator):
    
    
    model, desktop = LaunchCalcWithFile(XmlFileName)
    
    
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
    ShutdownCalc( desktop )
    
    
    pass

def ConvertToCsv( XmlFileName, CsvFileName, SheetName, Separator ):
    '''
    @param Separator: the delimiter, gets converted to the corresponding integer value
    '''
    converter = SSConverter()
    
    converter.convert( XmlFileName, CsvFileName, SheetName, ord( Separator ) )
