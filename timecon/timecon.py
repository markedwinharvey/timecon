#!/usr/bin/env python
'''
Convert between epoch time and datetime object

Usage:
	>>> import timecon as tc
	>>> a=tc.to_epoch(2012,12,25)
	>>> a
	1356422400
	>>> type(a)
	<type 'int'>
	>>> a=tc.from_epoch(a)
	2012-12-25 00:00:00
	>>> type(a)
	<type 'datetime.datetime'>
'''

from datetime import datetime as dt

def to_epoch(*time):
	try:
		if len(time) > 1:
			return int(dt(*time).strftime('%s'))
		if len(time) == 1:
			return time[0].strftime('%s')
		return 'Error: timecon requires time argument'
	except:
		msg = '''
		Error: could not convert time!
		Check for errors. 
		 Usage: 
		  timecon.to_epoch(yyyy,m,d[,h[,m[,s]]])  *or*
		  timecon.to_epoch(datetime object)
		  Dates preceding Jan. 1 1970 are meaningless. 
		'''.replace('\t','')
		return msg

def from_epoch(time):
	try:
		return dt.fromtimestamp(int(float(time)))
	except:
		msg = '''
		Error: could not convert time!
		Check for errors. 
		 Usage: 
		  timecon.from_epoch(1234567890)
		'''.replace('\t','')
		return msg	
	
