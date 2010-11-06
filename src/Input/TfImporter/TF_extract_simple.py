#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2010  <flindt@flindtathome.dyndns.org>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import csv

    
def DumpByTeacher(csvFile,  teacher):
    NewClassKeywords = ["ANTAL STUDERENDE:"]
    EndClassKeywords = ["I ALT", "I  ALT"]
    
    TfReader = csv.reader(open(csvFile), delimiter=',', quotechar='\"')
    TfWriter = csv.writer(open(teacher+'.csv',  'w'), delimiter=',', quotechar='\"' , quoting=csv.QUOTE_MINIMAL)
    
    state = 'FILEHEADER'
    lineno = 0
    classStartLine = 0
    classEndLine = 0
    for row in TfReader:
        lineno += 1
        if state in ['FILEHEADER',  'NEXTCLASS']:
            
            if len(row) > 5 :
                if row[0] in NewClassKeywords :
                    print "--> New class found"
                    state = 'CLASSHEADER'
                    classStartLine = lineno
                if  row[5] == "LÆRER":
                    print "--> New class found"
                    state = 'CLASSHEADER'
                    classStartLine = lineno - 1
        
        if state == 'CLASSHEADER':
            if lineno - 2 > classStartLine :
                state = 'INCLASS'
        
        if state == 'INCLASS':
            if row[0] in EndClassKeywords :
                state = 'CLASSFOOTER'
                classEndLine = lineno
        
        if state == 'CLASSFOOTER':
            if  lineno  > classEndLine:
                state = 'NEXTCLASS'
        
        
        # Writing to file is seperated from next-state logic for simplicity
        if state in ['FILEHEADER']:
            TfWriter.writerow(row)
        
        if state in ['CLASSHEADER']:
            TfWriter.writerow(row[:12])
        
        if state in ['INCLASS']:
            if len(row) > 5 :
                if row[5] == teacher :
                    TfWriter.writerow(row)
                    
        if state in ['CLASSFOOTER']:
            TfWriter.writerow([''])

    return 0


def main( csvfile = "./tf.csv",  teachers = ['MON',  'PFL']):
    for teacher in teachers:
        DumpByTeacher( csvfile, teacher )
    
    return 0


if __name__ == '__main__':
    main()
