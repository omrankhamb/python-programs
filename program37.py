"""Accepting Multiple Input"""

a,b,c = map(int,input("Enter Numbers :").split(','))        #getting Multiple inputs
print(a,b,c)                    

numbers = list(map(int,input("Enter List : ").split()))
print(numbers)

books = input("Enter books : ").split(',')
print(books)

print("Enter Time Stamp in hour:minute:seconds")
hour,minute,seconds = map(int,input("Enter timestamp : ").split(':'))
print(hour,minute,seconds)