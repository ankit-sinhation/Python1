#!/usr/bin/python

import commands
import sys
import os

#WAP In Py to delete multiple user.
#to use: python code6.py user1 user2 user3 (enter)

user_list=sys.argv[1: ]

for i in user_list :

	os.system('userdel -rf '+i)



