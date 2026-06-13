"""Delete operation"""
import os
try:
    os.remove('file.txt')       #File will be deleted
except Exception as e:
    print(f"Exception is :{e}") # If file not present then throws Exception

#Caheckinf file exist

import pathlib

file = pathlib.Path('file.txt')
if file.exists():
    print("File Not Deleted")
else:
    print("File deleted successfullly")