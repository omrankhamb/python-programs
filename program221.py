
# & opreator
def main()->None:
    iNo = int(input("Enter Number : "))
    iMask = 4096
    iAns = 0

    iAns = iNo & iMask

    if iAns == iMask : 
        print(f"13th bit is ON")
    else:
        print("13th  bit is OFF")


if __name__ == "__main__":
    main()