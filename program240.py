def ToggleBit(iNo : int , iPos :int)->int:
    iMask = 0x1
    iResult = 0

    if iPos < 1 or iPos > 32:
        print("Invalid position")
        return
    iMask = iMask << (iPos -1)
    iResult = iNo ^ iMask

    return iResult




def main()->None:
    iNo = 0
    iRet = 0
    iPos = 0


    iNo = int(input("Enter Number : "))
    iPos = int(input("Enter Bit Position : "))

    iRet = ToggleBit(iNo,iPos)
    print(f"Updated numebr is : {iRet}")



if __name__ == "__main__":
    main()