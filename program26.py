"""Pass By Value"""

def PassByValue(x):
    x = 24

a = 12
print(f"Before calling function :{a}")

PassByValue(a)
print(f"After calling a function : {a}")