""" Largest of Three Numbers"""

iNo =   int(input("Enter first Number :"))
iNo2 = int(input("Enter second Number : "))
iNo3 = int(input("Enter Three Number : "))


if(iNo > iNo2):
    if(iNo > iNo3):
        print(f"Number is greater : {iNo}")
    else:
       print(f"Number is greater : {iNo3}")
else:
    if(iNo2 > iNo3):
        print(f"Number is greater : {iNo2}")
    else :
        print(f"Number is greater : {iNo3}")