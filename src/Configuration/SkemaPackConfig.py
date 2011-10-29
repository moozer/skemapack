'''
Created on Sep 14, 2011

@author: flindt
'''
import exceptions
import os
import ConfigParser

class SkemaPackConfig(object):
    '''
    Holds all the configurations for skemapack
    
    Can be initialized from a file ( TODO ?: or a Dictionary)
    
    Look at http://docs.python.org/library/configparser.html for details on the config file syntax
    
    '''
    
    def __init__(self, ConfigFilename = ""):
        '''
        Constructor for loading configuration from a file
        '''
        if os.path.isfile(ConfigFilename):
            self._ConfigFileName = ConfigFilename
        elif os.path.isfile("skemapack.cfg"):
            self._ConfigFileName = "skemapack.cfg"
        elif os.path.isfile(os.path.expanduser("~/.skemapack/skemapack.cfg")):
            self._ConfigFileName = os.path.expanduser("~/.skemapack/skemapack.cfg")
        else:
            raise exceptions.ValueError
        
        self._ConfigParser = ConfigParser.ConfigParser()
        self._ConfigParser.read(self._ConfigFileName)
        
        self.get = self._ConfigParser.get
        
        
        
    def __str__(self):
        PrintString = '## Config used\n'
        for Section in self._ConfigParser.sections():
            PrintString += "# ["+ Section + "]\n"
            for key in self._ConfigParser.items(Section):
                PrintString += "# " + key[0] + " = " + key[1] + "\n"
        PrintString += "#\n"
                
        return PrintString
            
    