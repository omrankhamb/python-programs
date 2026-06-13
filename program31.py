"""File opening and reading"""

with open('file.txt','r') as f:
    print(f.read())         # Read Whole File
    print(f.readline())     # Print only firstline
    print(f.readline())     # Now print second line
    print(f.readlines())    # Now give the content of file line by line in list


