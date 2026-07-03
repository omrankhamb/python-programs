
# & opreator
def main()->None:
    iNo = int(input("Enter Number : "))
    iMask = 64
    iAns = 0

    iAns = iNo & iMask

    if iAns == iMask : 
        print(f"7th bit is ON")
    else:
        print("7th  bit is OFF")


if __name__ == "__main__":
    main()