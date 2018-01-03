#!/usr/bin/python

import commands
import webbrowser

#WAP In Py to Display The IpAdress Of Other Systems Connected To The Same Localnet.

print "The Connected MAC's Are...."
print "		"
print "		"


z=commands.getoutput('arp-scan -I wlo1 -l | grep -i 192.168.')
z=z.splitlines()
t=[]

for i in z :

	a=i.split('\t')
	t.append(a)

for i in range(0,len(t)) :

	print t[i][1]



