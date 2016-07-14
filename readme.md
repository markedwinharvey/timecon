<h4>timecon</h4>
<h5>easy conversion between epoch time and datetime object</h5>

<h6>
	timecon.to_epoch(args) accepts date/time tuple or datetime object
	and delivers integer-value epoch time
	
	timecon.from_epoch(args) accepts integer-value epoch time 
	and delivers datetime object
</h6>

Installation:

	python setup.py install

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
