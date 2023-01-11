import os 

def create_evil_file(): 
    '''creates a file named "evil.py" which can act as a rootkit virus'''
    evil_string = """ 
#!/usr/bin/python
 
import os
import sys
import subprocess
 
#Add some malicious functions in here 
 
#Carry out some system changes and hide them from the user
subprocess.Popen("echo 'This is a hidden message' >> /etc/syslog",shell=True)
subprocess.Popen("echo 'This is a hidden message 2' >> /var/log/term.log", shell=True)
subprocess.Popen("echo 'This is a hidden message 3' >> /var/spool/mail/root", shell=True)
subprocess.Popen("echo 'This is a hidden message 4' >> /etc/issue", shell=True)
"""
    f = open("evil.py", "w") 
    f.write(evil_string) 
    f.close() 
     
create_evil_file()