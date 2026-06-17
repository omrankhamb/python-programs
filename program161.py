# File n=handling

with open('file.txt','a') as f:
    no = int(input("Enter number tp store data :"))
    f.write("Name,Age,Salary\n")
    for i in range(no):
        name = str(input("Enter name :\n"))
        age = int(input("Enter age : \n"))
        salary = int(input("Enter salary : \n"))
        f.write(f"{name},{age},{salary}\n\n")
    f.close()

with open('file.txt','r') as f:
    lines = f.read()
    f.close()
    print(lines)

with open('file.txt','w') as f:
    sStr = str(input("Enter name to delete data : "))
    for line in lines:
        print(line)

    f.write(sStr)

    


