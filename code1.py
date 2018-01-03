#!/usr/bin/python

import commands

print "If You Enter A Number Greater Than 25; It Will Show You The Date."
print "   "
print "If You Enter A Number Less Than 25; It Will Open A New Terminal For 10secs."
print "   "

x=raw_input(" Enter a Number: ")
print "   "

if int(x) > 25 :

	print (commands.getoutput('date'))

else :

	commands.getoutput('gnome-terminal -x sleep 10s;exit')

