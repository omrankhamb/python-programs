"""
    String Built in function
"""
from Package.StringX import StringX

def main():
    sString = str(input("Enter String : "))

    sRet = ""
    iRet = 0
    sobj = StringX()

    cValue = str(input("Enter Charcter To Find in string : "))

    # Character Present in string or not
    if sobj.FindX(sString,cValue):
        print(f"{cValue} Present in String ")
    else:
        print(f"{cValue} Not present in string")


    # Length of String
    iRet = sobj.LengthX(sString)
    print(f"Length of String : {iRet}")

    # Converting Upper Of string
    sRet = sobj.UpperX(sString)
    print(f"Upper of String : {sRet}")

    # Converting Lower Of string
    sRet = sobj.LowerX(sString)
    print(f"Lower of String : {sRet}")

    # Reverse Of String
    sRet = sobj.ReverseX(sString)
    print(f"Reverse of String : {sRet}")


if __name__ == "__main__":
    main()