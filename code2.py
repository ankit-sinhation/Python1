#!/usr/bin/python

import commands
import webbrowser
print " WAP In Py to Display The Result Of Five Inputs."
print " If The Input Is A Command; Then Show The Result Of The Command."
print " If Its Not A Command; Simply Display The Input."
print "		"
print "		"
print " Input 5 things to know their output. "

x= []

for a in range(1,6) :

	a=raw_input(' enter {}:   '.format(a))

	x.append(a)



for i in x :

	z=commands.getoutput('ls /usr/bin | grep -w {}'.format(i))

	if z == i :

		print (commands.getoutput(i))

	else :

		print i

	
