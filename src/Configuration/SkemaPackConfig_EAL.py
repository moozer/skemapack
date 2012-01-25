#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
Created on Jan 25, 2012

@author: poul
'''

import SkemaPackConfig

if __name__ == '__main__':
    myConfig = SkemaPackConfig.SkemaPackConfig(SkemaPackConfig.SkemaPackConfig_stdin_eal())
    print myConfig
    pass