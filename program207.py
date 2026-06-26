"""
    String Built in function
"""

import sys
def main():
    sString = str(input("Enter String : "))
    print(f"{sString}")
    print(sys.getsizeof(sString))

if __name__ == "__main__":
    main()