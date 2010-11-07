SkemaToIcs.py 
-------------
Try running it with -h and you will get the list of parameters
Perhaps you need to set up your PYTHONPATH properly

On my machine
export PYTHONPATH=~/EclipseDev/skemapack/src/:~/EclipseDev/skemapack/src/Support/iCalendar-1.2/src/


Example:

SkematoIcs.py -u http://skema.sde.dk/laererSkema.aspx?idx=5421&lang=da-DK

and the ics data is dumped in SkemaCurrentWeek.ics

