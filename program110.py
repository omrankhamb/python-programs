"""
    Delete Specific line from file 
"""

with open('file.txt','r') as file:
    str = file.readlines()
    file.close()

with open('file.txt','w') as file:
    for line in str:
        if 'Omprasad' in line:
            str.remove(line)
    str = "".join(str)
    file.writelines(str)



