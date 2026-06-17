"""
    WAP to calculate the square of only those numbers whose least significant digit is 5 
"""
def SquareofSignificantdigit(iNo:int):
    lsb = iNo % 10
    if lsb == 5:
        return iNo * iNo
    else :
        return -1

iValue = int(input("Enter Number : "))
iRet = SquareofSignificantdigit(iValue)

if (iRet == -1):
    print("Rule are not match")
else:
    print(f"Suare of number is : {iRet}")





