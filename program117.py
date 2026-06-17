"""
    Read the string “hello world” from the user. Make use of continue keyword and 
    remove space  
"""

def RemoveSpaceString(sStr: str)->str:
    str = ""
    for i in sStr:
        if i == ' ':
            continue
        else :
            str = str + i

    return str

sStr = str(input("Enter String : "))
sStr = RemoveSpaceString(sStr)
print(f"After Removing string : {sStr}")