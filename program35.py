"""Exception Handling"""

a = 23
b = 0

try :
    x = a//b
    print(f"Division of {a} and {b} is : {x}")  #ZeroDivisionError: division by zero exception
except Exception as e:
    print(f"Exception is :{e}")
finally:
    print("Code runs successfully")



