""" Nesting of loop"""

i = int(input("Enter Number : "))
j = int(input("Enter number : "))

# Nested loop
for k in range(i+1):
    for l in range(k+1):
        print("*",end="")
    print()