# position 13
def main()->None:
    iNo = 0
    iMask = 0xFFFFEFFF
    iPos = 0

    iNo = int(input("Enter Numeber : "))
    iNo = iNo & iMask

    print(f"Updated number is :{iNo}")

if __name__ == "__main__":
    main()