'''
Created on May 18, 2011

@author: morten
'''

def AppendSrcToPythonPath():
    import sys, os
    this_dir = os.path.abspath(__file__)
    while 1 == 1:
        this_dir, tail = os.path.split(this_dir)
        if tail == 'src': # always go to src as default dir.
            this_dir = os.path.join(this_dir, tail) 
            break
    sys.path.append(this_dir) 
    sys.path.append(os.path.join(this_dir, 'Support/iCalendar-1.2/src')) 
    
# an use it
AppendSrcToPythonPath()