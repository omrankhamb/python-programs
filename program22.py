"""Arbitrary Arguments in python"""

def Arbitrary (*args):
    print("Arbitrary arguments are : ")
    for arg in args:
        print(arg)


Arbitrary('om','soham','pranav','harsh','Mangesh')

def ArbitraryX(**Kwargs):
    print("Dictionary is :")
    for Key,value in Kwargs.items():
        print(f"{Key} {value}")

ArbitraryX(name = "soham",salary = 2400)

