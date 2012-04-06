'''
Created on Apr 4, 2012

@author: flindt
'''
import unittest
import os
import time
import uno
import unohelper

from com.sun.star.beans import PropertyValue

@unittest.skip("fails and stalls unittesting")    
class Test(unittest.TestCase):


    def setUp(self):
           
    
        Cmd = "libreoffice"
        Cmd = '%s --headless --norestore "--accept=socket,host=localhost,port=2002;urp;"'%(Cmd)
           
        print "issuing: %s"%Cmd
        # os.system( Cmd ) wont work, since it wait for the process to end...
        os.popen(Cmd)
        time.sleep(0.5)
        
        # get the uno component context from the PyUNO runtime
        self.localContext = uno.getComponentContext()
        
        # create the UnoUrlResolver
        self.resolver = self.localContext.ServiceManager.createInstanceWithContext(
                        "com.sun.star.bridge.UnoUrlResolver", self.localContext )
        
        # connect to the running office
        self.ctx = self.resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
        self.smgr = self.ctx.ServiceManager
        
        # get the central desktop object
        self.desktop = self.smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",self.ctx)
        
        # access the current calc document
        self.model = self.desktop.getCurrentComponent()
        pass


    def tearDown(self):
        
        time.sleep(0.5)
        self.model.dispose()
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()