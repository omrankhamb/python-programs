"""
    To keep record of patients’ medical data, manipulate files to store, update, and 
    delete such information.
"""

iNo = int(input("Enter number To store Data in values"))

for _ in range(iNo):
    with open('file.txt','a') as file:
        name = str(input("Enter Patients Name :\n"))
        age = int(input("Enter Age : \n"))
        day = int(input("Enter Day : \n"))
        file.write(f"Name : {name}|Age : {age}|Day : {day}\n")
    file.close()

with open('file.txt','r') as file:
    lines = file.readlines()
    file.close()

with open('file.txt','w') as file :
    name = str(input("Enter a name to delete a data : "))
    for line in lines:
        if name in line:
            lines.remove(line)
    lines = "".join(lines)
    file.write(lines)
            



