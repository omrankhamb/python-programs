"""
    Delete Specific word from file 
"""

with open('file.txt','r+') as file:
    str  = file.read()
    print(str)
    str = str.replace("Omprasad","")
    file.seek(0)
    file.write(str)



