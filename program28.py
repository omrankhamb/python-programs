"""file Handling"""

file = open('file.txt','a')                     # IF file Not present then creta afile

print(f"Name of File is : {file.name}")         # file.txt
print(f"Mode of Opening File : {file.mode}")    # Append mode
print(f"Status of file : {file.closed}")        # False

file.close()
print(f"Status of file : {file.closed}")        # True
