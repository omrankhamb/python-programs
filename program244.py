# position 13

def OffBit(iNo : int,iPos : int)->int:
    iMask = 0x1
    iResult = 0

    if iPos < 1 or iPos > 32 :
        print("Invalid Bit position")
        return iNo
    
    iMask = iMask << (iPos - 1)
    iMask = ~iMask
    iResult = iNo & iMask

    return iResult

def main()->None:
    iValue = 0
    iRet = 0
    iLocation = 0

    iValue = int(input("Enter number : "))
    iLocation = int(input("Enter the bit position : "))

    iRet = OffBit(iValue,iLocation)
    print("Updated number is : ",iRet)
    
if __name__ == "__main__":
    main()