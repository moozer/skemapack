#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 28 Jan 2012

@author: moz
'''
from Datatypes.EventFunctions import ReadString
from Configuration.SkemaPackConfig import SkemaPackConfig, SkemaPackConfig_stdin_eal
import sys
from Export.ExportFile import ExportFile


def ImportTfZip( config = None, ConfigSet = "ImportFile" ):
    '''
    Imports events and config from file (or stdin)
    @param config: The config object to use. If None, then we try to use defaults or stdin
    @param ConfigSet: The section of the configuration to use
    @raise KeyError: If supplied ConfigSet is not in config
    @return: (events, config) or (weeksums, config) 
    '''  
    return [], config

