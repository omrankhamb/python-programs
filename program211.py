
# printing binary number system
def main():
    iNo = int(input("Enter Number : "))

    while iNo != 0 :
        print(iNo%2,end="")
        iNo = iNo // 2


if __name__ == "__main__":
    main()