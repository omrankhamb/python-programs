
def main()->None:
    iNo = 0
    iMask  = 0x1
    iPos = 0

    iNo = int(input("Enter Number : "))
    iPos = int(input("Enter Bit Position : "))

    iMask = iMask << (iPos - 1)
    iNo = iNo ^ iMask

    print(f"Updated number is : {iNo}")

if __name__ == "__main__":
    main()