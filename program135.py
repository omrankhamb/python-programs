"""
    CheckPrime
"""
def CheckPrime(iNo : int)->bool:
    icount = 2
    for i in range(2,(iNo //2 )+1):
        icount +=1
        if iNo % i == 0:
            break
    
    if icount == (iNo//2) + 1 :
        return True    
    else :
        return False

    
iValue = int(input("Enter Number : "))
iRet = CheckPrime(iValue)

if iRet : 
    print(f"Number is Prime {iValue}")
else:
    print(f"Number is not prime {iValue}")
