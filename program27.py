"""Pass by efrence"""

a= [10]

def PassByRefrence(x):          # Accepet only Array as a input
    x[0] = 20


print(f"Before calling function :{a}")
PassByRefrence(a)
print(f"After calling a function : {a}")


#PassByRefrence(33)              # 'int' object does not support item assignment