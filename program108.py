"""
    To keep record of patients’ medical data, manipulate files to store, update, and 
    delete such information.  
"""

with open('file.txt','r') as file:
    str  = file.read()
    print(str)
    file.close()

with open('file.txt','w') as file :
    file.write(str)



