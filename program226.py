
# & opreator
def main()->None:
    iMask = 0x1
   
    print(f"{hex(iMask)}")       # 1
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 2
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 3
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 4
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 8
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 16
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 32
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 64
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 128
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 256
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 512
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 1024
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 2048
    iMask = iMask << 1

    print(f"{hex(iMask)}")       # 4096
    iMask = iMask << 1

if __name__ == "__main__":
    main()