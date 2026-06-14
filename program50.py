# Create Package and Getting Value From Package
from Package import greet
from Package.Addition import Addition

# Function From Package __init__.py 
greet()

# Function from Package Addition.py
# Where Addition Is SubPackage
iRet = Addition(10,12)
print(iRet)