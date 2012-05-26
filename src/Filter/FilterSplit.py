#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 26 May 2012

@author: moz
'''

def FilterSplit( Events, config = None, ConfigSet="FilterSplit" ):
    
    Teacher = config.get(ConfigSet, "Teacher")
    
    res = []
    for e in Events:
        if e['Teacher'] == Teacher:
            res.append(e)
            
    return res, config


