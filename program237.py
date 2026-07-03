
# Position at bit 11
def main()->None:
    iNo  = 0
    iMask = 0

    iNo = int(input("Enter number : "))

    iMask = 0x400
    iNo = iNo ^ iMask

    print(f"Updated number is : {iNo}")

if __name__ == "__main__":
    main()