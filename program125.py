"""
    Python Program to Find HCF or GCD
"""

def GCD(a : int,b : int)->int:
    if (b== 0) :
        return a
    return GCD(b,a%b)

iNo,iNo2 = map(int,(input("Enter two number to find GCD and lcm : ").split(',')))

iRet = GCD(iNo,iNo2)
lcm = (iNo2* iNo) // iRet
print(f"GCD/HCF is : {iRet}\nlcm is : {lcm}")