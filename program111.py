"""
    Get a data from user and get a particular data by name
"""

iNo = int(input("Enter number To store Data in values"))

for _ in range(iNo):
    with open('file.txt','a') as file:
        name = str(input("Enter Name :\n"))
        age = int(input("Enter Age : \n"))
        day = int(input("Enter Day : \n"))
        file.write(f"Name : {name}\nAge : {age}\nDay : {day}\n\n")
    file.close()

name = str(input("Enter Name to get data of Student : "))
with open('file.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        if name in line:
            print(line,lines[1],lines[2])



