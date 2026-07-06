# position of 3 & 7
# position of 3 & 7
def main()->None:
    iMask = 0x00000044
    iNo = 0
    iResult = 0

    iNo = int(input("Enter Number : "))
    iResult = iNo ^ iMask
    print(f"Updated number is : {iResult}")
if __name__ == "__main__":
    main()