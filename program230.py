
# & opreator
def main()->None:
    iMask = 0x1
   
    for i in range(1,33):
        print(f"{i} : {hex(iMask)}")
        iMask = iMask << 1

if __name__ == "__main__":
    main()