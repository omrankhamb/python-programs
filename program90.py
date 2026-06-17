"""
    Program to check whether a given key already exists in a dictionary. 
"""
dic = {
    "Name" : "omprasad",
    "age" : 19,
    "City" : "Latur",
    "Village" : "Khulgapur"
}

def KeyPresentOrNot(dic : dict ,Key)->bool:
    for I in dic.keys():
        if I == Key :
            return True
    return False

Key = str(input("Enter String :"))
ans = KeyPresentOrNot(dic,Key)
if ans == True :
    print("Key is Present")
else :
    print("Key not Present")

