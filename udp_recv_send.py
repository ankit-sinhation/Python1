#!/usr/bin/env python2

import  socket,thread
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# This Program Should Be Executed By The Reciever.
#                    ip_type(ipv4) ,  proto_type (UDP)
x.bind(("",8888))
#  Enter the IP from which you have to recve messages.
sender_ip="192.168.10.186"
sender_port=9999
#  default ip is binded with port 9999 

def  recv():
        while True:
		# 1000 is the words to which you can chat. 
                # you can also extend the 1000 to more for more chats.
                data=x.recvfrom(1000)
                print  data[0]


def  send():
        while True:
                rply=raw_input("type here:   ")
                x.sendto(rply,(sender_ip,sender_port))

thread.start_new_thread(recv,())
thread.start_new_thread(send,())

while True:
	pass
