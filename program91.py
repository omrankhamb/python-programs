"""
    Python Program to Convert Decimal to Binary, Octal and Hexadecimal using 
    anonymous function.
"""
def decimalToBinary(iNo):
    return bin(iNo)

def OctalToHexadecimal(iNo2):
    return hex(iNo2)


iNo = int(input("Enter Decimal Number : "))
iNo2 = str(input("Enter Octal Number : "))

iBin = decimalToBinary(iNo)
iBin2 = OctalToHexadecimal(iNo2)

print(f"{iNo} decimal to binary is : {iBin}")
print(f"{iNo2} octadecimal to hexadecimal is : {iBin2}")



