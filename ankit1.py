#!/usr/bin/python

import commands
import webbrowser

#web browser library will open default browser of os

print " Enter Any Number."
print " If You Enter A Number Greater Than 30; It Will Open A New Terminal."
print " If You Enter A Number Greater Than 20 And Less Than 30; It Will Open The Date."
print " If You Enter A Number Less Than 20; It Will Ask You To Search Anything On Youtube."
print "				"
print "				"

x=raw_input("Type A Number: ")


if int(x) > 20 and int(x) < 30 :

	print commands.getoutput('date')

elif int(x) > 30 :

	print commands.getoutput('gnome-terminal')

else :
	add= "https://www.youtube.com/results?search_query="

	y=raw_input(" Type Anything You Want To Search On Youtube: ")

	print " Plz Wait, Youtube Is Loading... "

	z = add + y
	print " 					"
	print "						"
	print "						"
	print "						"
	print "Opening: ", z
	print "						"
	print "						"
	print "						"
	print "						"

	webbrowser.open_new_tab(z)
	
