#!/usr/bin/python

import commands
import sys
import os

#WAP In Py to create multiple user.
#to use: python code5.py user1 user2 user3 (enter)

user_list=sys.argv[1: ]

for i in user_list :

	os.system('useradd '+i)



