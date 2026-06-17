"""
    Write a Python program that reads a text file, counts the number of words in it, and 
    writes the word count to a new file. 
"""

with open('file.txt','r') as file:
    str = file.readline()
    str  = str + file.readline()
    str = str + file.readline()
    file.close()
    
with open('file2.txt','w') as file:
    file.write(f"Length of String is : {len(str)}")
    file.close()



