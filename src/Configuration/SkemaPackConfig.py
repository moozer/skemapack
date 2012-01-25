#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Sep 14, 2011

@author: flindt
'''
import exceptions
import os
import ConfigParser
import sys

class SkemaPackConfig_stdin(object):
    '''
    This class reads from STDIN
    '''
    
    def __init__(self):
        self.name="STDIN"
        pass
    
    def readline(self):
        thisLine = sys.stdin.readline()
        return thisLine        
    
class SkemaPackConfig_stdin_eal(object):
    '''
    This class reads from STDIN and strips the first # on each line.
    The first line with no # is EOF
    '''
    
    def __init__(self):
        self.name="STDINEAL"
        pass
    
    def readline(self):
        thisLine = ""
        try:
            thisLine = sys.stdin.readline().split('#')[1].strip()
        except IndexError:
            return None         # No more configuration lines 
        return thisLine        
    

class SkemaPackConfig(object):
    '''
    Holds all the configurations for skemapack
    
    Can be initialized from a file ( TODO ?: or a Dictionary)
    
    Look at http://docs.python.org/library/configparser.html for details on the config file syntax
    
    '''
    
    def __init__(self, ConfigFilename = SkemaPackConfig_stdin()):
        '''
        Constructor for loading configuration from a file
        '''
       
        self._ConfigParser = ConfigParser.ConfigParser()
        self._ConfigParser.readfp(ConfigFilename)
        
        self.get = self._ConfigParser.get
        
        
        
    def __str__(self):
        #PrintString = '## Config used\n'
        PrintString = ""
        for Section in self._ConfigParser.sections():
            PrintString += "# ["+ Section + "]\n"
            for key in self._ConfigParser.items(Section):
                PrintString += "# " + key[0] + " = " + key[1] + "\n"
        PrintString += "#\n"
                
        return PrintString
    
    
if __name__ == "__main__":
    myConfig = SkemaPackConfig()
    print myConfig
    
            
    