
# & opreator
def main()->None:
    iNo = int(input("Enter Number : "))
    iMask = 0x1
    iAns = 0
    iPos = int(input("Enter BIT position to find : "))

    iMask = iMask << (iPos -1)
    iAns = iNo & iMask

    if iAns == iMask :
        print(f"{iPos} bit is ON")
    else:
        print(f"{iPos} BIT Is OFF")


if __name__ == "__main__":
    main()