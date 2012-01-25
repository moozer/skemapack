#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
Created on Jan 25, 2012

@author: poul

This file is an example of how to use the SkemaPackConfig package to read EAL options from the command line
'''

import SkemaPackConfig

import sys

if __name__ == '__main__':
    myConfig = SkemaPackConfig.SkemaPackConfig(SkemaPackConfig.SkemaPackConfig_stdin_eal())
    print myConfig
    
    print sys.stdin.readlines()
    pass