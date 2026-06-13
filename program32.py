"""File opening and Writing"""

with open('file.txt','w') as f:
    # Write the data in file
    f.write("Hi my name is omprasad")   
    # Write the data in file line by line                
    f.writelines(["Hi my name is omprasad\n","I am from latur\n","i Am new in pune\n"])




