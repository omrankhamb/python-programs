
# & opreator
def main()->None:
    iNo = int(input("Enter Number : "))
    iMask = 0x00010000
    iAns = 0

    iAns = iNo & iMask

    if iAns == iMask : 
        print(f"17th bit is ON")
    else:
        print("17th  bit is OFF")


if __name__ == "__main__":
    main()