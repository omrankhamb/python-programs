"""
    Create a function to calculate square and cube of a number and return Multiple 
    Values from a Function.
"""


def AreaAndCircumgerenceOfCircle(iRadius :float)->float:
    Area = (iRadius ** 2) * 3.14
    Circumference = 2 * (3.14) * (iRadius)

    return Area , Circumference

fRadius = float(input("Enter Number : "))
Square,Circumference = AreaAndCircumgerenceOfCircle(fRadius)
print(f"Area = {Square}\nCircumference = {Circumference}")


