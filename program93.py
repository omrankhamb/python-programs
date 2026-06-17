"""
    WAP to read a 4-digit number through the keyboard and calculate sum of digits. 
"""
# Sum of 4 digit number
def SumOfDigitOfNumber(iNo : int)->int:
    iSum = 0

    while iNo != 0:
        iSum = iSum + (iNo % 10) 
        iNo = iNo //10

    return iSum

iNumber = int(input("Enter Number : "))
iRet = SumOfDigitOfNumber(iNumber)
print(f"Sum of digit Of Number {iNumber} is {iRet}")

