"""
    Create a function to calculate square and cube of a number and return Multiple 
    Values from a Function.
"""


def SquareAndCube(iNO):
    return iNO**2,iNO**3

ino = int(input("Enter Number : "))
Square,Cube = SquareAndCube(ino)
print(f"Square and cube of {ino} is {Square} {Cube}")


