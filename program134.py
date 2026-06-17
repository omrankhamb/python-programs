"""
    CheckPrime
"""
def CheckPrime(iNo : int)->bool:
    flag = True
    for i in range(2,(iNo //2 )+1):
        if iNo % i == 0:
            flag = False
            break
    
    if flag :
        return True    
    else :
        return False

    
iValue = int(input("Enter Number : "))
iRet = CheckPrime(iValue)

if iRet : 
    print(f"Number is Prime {iValue}")
else:
    print(f"Number is not prime {iValue}")
