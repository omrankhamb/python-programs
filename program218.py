
# & opreator
def main()->None:
    iNo = int(input("Enter Number : "))
    iMask = 4
    iAns = 0

    iAns = iNo & iMask

    if iAns == iMask : 
        print(f"3rd bit is ON")
    else:
        print("3rd bit is OFF")


if __name__ == "__main__":
    main()